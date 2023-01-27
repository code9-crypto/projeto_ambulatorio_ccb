import sys
from cx_Freeze import setup, Executable

base  = None

if sys.platform == "win32":
    base = "win32GUI"

executables = [
    Executable("login.py", base = base)
]

includeFiles = ["img/", "banco/"]

setup(
    name = "Ambulatório",
    version = "1.0",
    description = "Sistema usado na congregação",
    options = {"build_exe":{"include_files":includeFiles}},
    executables=executables
)

