#!/bin/python3
import shutil

# shutil.copyfile(src, dst, *, follow_symlinks=True)    
# Copy the contents (no metadata) of the file named src to a file named dst and return dst. src and dst are path names given as strings. dst must be the complete target file name; look at shutil.copy() for a copy that accepts a target directory path. If src and dst specify the same file, SameFileError is raised.

# shutil.copyfileobj(fsrc, fdst, length=16*1024)    
# Copy the contents of the file-like object fsrc to the file-like object fdst. The integer length, if given, is the buffer size. In particular, a negative length value means to copy the data without looping over the source data in chunks; by default the data is read in chunks to avoid uncontrolled memory consumption. Note that if the current file position of the fsrc object is not 0, only the contents from the current file position to the end of the file will be copied.

# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)   
# Recursively copy an entire directory tree rooted at src. The destination directory, named by dst, must not already exist; it will be created as well as missing parent directories. Permissions and times of directories are copied with copystat(), individual files are copied using shutil.copy2().

# shutil.move(src, dst, copy_function=copy2)   
# Recursively move a file or directory (src) to another location (dst) and return the destination. If the destination is an existing directory, then src is moved inside that directory. If the destination already exists but is not a directory, it may be overwritten depending on os.rename() semantics. If the destination is on the current filesystem, then os.rename() is used. Otherwise, src is copied (using shutil.copy2()) to dst and then removed. In case of symlinks, a new symlink pointing to the target of src will be created in or as dst and src will be removed. If the optional symlinks flag is true, symbolic links in the source tree are represented as symbolic links in the new tree and the metadata of the original links will be copied as far as the platform allows; if false or omitted, the contents and metadata of the linked files are copied to the new tree.

# shutil.rmtree(path, ignore_errors=False, onerror=None)  
# Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory). If ignore_errors is true, errors resulting from failed removals will be ignored; if false or omitted, such errors are handled by calling a handler specified by onerror or, if that is omitted, they raise an exception.