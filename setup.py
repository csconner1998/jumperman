import cx_Freeze

executables = [cx_Freeze.Executable("F:\Code\GAME LUL\MAIN.py")]

cx_Freeze.setup(
    name="JUMPERMAN",
    options={"build_exe": {"packages":["pygame"]}},
    executables = executables

    )
