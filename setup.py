import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

buildOptions = {
        'includes': 'atexit',
        "replace_paths": [("*", "")]
}

executables = [
    Executable("main.py", base=base)
]

setup(
    name="Championnat",
    version="0.1",
    description="Gestion pour la création d'un championnat avec statistique",
    options=dict(build_exe=buildOptions),
    executables=executables
)
