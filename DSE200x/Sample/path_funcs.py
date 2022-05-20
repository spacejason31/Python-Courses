import pathlib
path = pathlib.Path()
print(repr(path))
path = pathlib.Path(".")
new_path = path / "folder" / "folder" / "example.py"

p = pathlib.Path("")
txt_files = p.glob("*.txt")
print("*.txt:", list(txt_files))
print("**/*.txt", list(p.glob("**/*.txt")))
print("*/*:", list(p.glob("*/*")))
print("Files in */*:", [f for f in p.glob("*/*") if f.is_file()])
txt_files = p.glob("*.txt")
list(txt_files)
list(p.glob("**/*.txt"))
list(p.glob("*/*"))
[f for f in p.glob("*/*") if f.is_file()]
txt_files = list(p.glob("*.txt"))
txt_files

import pathlib
p = pathlib.Path.home()
list(p.glob(".*"))
list(p.glob(".c*"))

import subprocess
subprocess.run(["dir"], shell=True)
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print("stdout:", result.stdout)
print("stderr:", result.stderr)
result = subprocess.run(["dir", "-l"], shell=True, capture_output=True, text=True)
print("stdout:", result.stdout)

import subprocess
result = subprocess.run(["env"], shell=True, capture_output=True, text=True)
print(result.stdout)