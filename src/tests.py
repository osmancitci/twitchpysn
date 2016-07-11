# pybot tests

import py_compile
import os

src = ""
if ("\\pybot\\src" in os.getcwd()):
    src = os.getcwd()
else:
    src = os.path.join(os.getcwd(), "src")

def main():
    # Compile code to make sure its syntactically correct
    print("[PYBOT TESTS]\n")
    print("[TEST 1] Simple syntax check")
    compileTest()

def getPyFilesFromDir(dir = ""):
    loc = os.path.join(src, dir)
    print("looking in " + loc)
    return [os.path.join(dir, f) for f in os.listdir(loc) if os.path.isfile(os.path.join(loc, f)) and ".py" in f and not ".pyc" in f and not "py." in f] # todo regex

def compileTest():
    print("Filding files...")
    subfolders = [s[0] for s in os.walk(src)]
    files = []
    files.extend(getPyFilesFromDir(src))
    for folder in subfolders:
        files.extend(getPyFilesFromDir(folder))
    print("compiling files...")
    for file in files:
        py_compile.compile(file, doraise=True)
        print(file + " compiled with no errors")

if __name__ == "__main__":
    main()