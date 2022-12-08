import pathlib

path1 = pathlib.Path("/images/whatsApp/hello.txt")
path2 = pathlib.Path.cwd()
path3 = path2 / "private.jpg"

print(path1.is_absolute())
print(path1)
print(path2)
print(path3)
