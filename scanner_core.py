# scanner_core.py
import os
import ctypes
import stat
from ctypes import wintypes

# WinAPI Constants
IO_REPARSE_TAG_MOUNT_POINT = 0xA0000003
FILE_ATTRIBUTE_REPARSE_POINT = 0x400

def _get_reparse_tag(path):
    # Dùng WinAPI để lấy Tag thật (0xa0000003, ...)
    CreateFileW = ctypes.windll.kernel32.CreateFileW
    DeviceIoControl = ctypes.windll.kernel32.DeviceIoControl
    CloseHandle = ctypes.windll.kernel32.CloseHandle
    handle = CreateFileW(path, 0x80000000, 7, None, 3, 0x02200000, None)
    if handle == wintypes.HANDLE(-1).value: return None
    buf = ctypes.create_string_buffer(1024)
    returned = wintypes.DWORD()
    ok = DeviceIoControl(handle, 0x900a8, None, 0, buf, len(buf), ctypes.byref(returned), None)
    CloseHandle(handle)
    return int.from_bytes(buf.raw[0:4], "little") if ok else None

def scan(root, log_func=print, progress_func=None):
    result = {"dirs_scanned": 0, "reparse": 0, "zombie": 0}
    visited_ids = set()

    log_func(f"[START SCAN] {root}\n")

    # BƯỚC 1: ĐẾM NHANH (Fast Count) để lấy Total cho Progress
    total_dirs = 0
    if progress_func:
        log_func("[INFO] Calculating workload...\n")
        for _, dirs, _ in os.walk(root):
            total_dirs += len(dirs)
        total_dirs = max(1, total_dirs)

    # BƯỚC 2: QUÉT THẬT
    current_idx = 0
    for current, dirs, files in os.walk(root, topdown=True):
        try:
            # Chặn Loop bằng File ID
            st_info = os.stat(current)
            f_id = (st_info.st_dev, st_info.st_ino)
            if f_id in visited_ids:
                dirs[:] = []
                continue
            visited_ids.add(f_id)
            
            result["dirs_scanned"] += 1

            for d in list(dirs):
                full = os.path.join(current, d)
                current_idx += 1
                
                # Cập nhật Progress Bar
                if progress_func:
                    progress_func(current_idx, total_dirs)

                try:
                    lst = os.lstat(full)
                    if lst.st_file_attributes & FILE_ATTRIBUTE_REPARSE_POINT:
                        tag = _get_reparse_tag(full)
                        kind = "JUNCTION" if tag == IO_REPARSE_TAG_MOUNT_POINT else "REPARSE"
                        
                        # Kiểm tra ZOMBIE (đường dẫn đích không tồn tại)
                        if not os.path.exists(full):
                            result["zombie"] += 1
                            log_func(f"[ZOMBIE]  {full}\n")
                        else:
                            result["reparse"] += 1
                            log_func(f"[REPARSE] {full}\n          TYPE: {kind}\n          TAG : {hex(tag) if tag else '?'}\n\n")
                        
                        dirs.remove(d) # Không quét sâu vào Junction/Reparse
                except:
                    # Lỗi lstat thường là folder ma hoặc quyền truy cập
                    result["zombie"] += 1
                    log_func(f"[ZOMBIE]  {full} (Inaccessible)\n")
                    dirs.remove(d)
        except:
            continue

    log_func("\n====== REPORT ======\n")
    log_func(f"DIRS SCANNED : {result['dirs_scanned']}\n")
    log_func(f"REPARSE     : {result['reparse']}\n")
    log_func(f"ZOMBIE      : {result['zombie']}\n")
    log_func("====================\n")