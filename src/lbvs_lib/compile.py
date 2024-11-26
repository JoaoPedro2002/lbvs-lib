"""
Only import ctypes once, repeated imports may call a cached version of the library,
causing inconsistent c struct mappings
"""
import ctypes
import os

file_path = __file__.replace("compile.py", "shared_lib.so")
if not os.path.exists(file_path):
    import subprocess
    make_process = subprocess.Popen(f"make clean shared-lib", shell=True, cwd=os.path.dirname(file_path))
    if make_process.wait() != 0:
        raise Exception(make_process.poll())

shared_library = ctypes.CDLL(file_path)



"""
Constants for the voting scheme
TODO: get these values from the C code
"""

# Commitment scheme
NONZERO = 36
BETA = 1
WIDTH = 3
HEIGHT = 1

# Encryption scheme
DIM = 2

# Vericrypt
VECTOR = 3

# Params
MODP = 3906450253
DEGREE = 1024
DEGCRT = DEGREE >> 1
SIGMA_C = 54000
SIGMA_E = 54000