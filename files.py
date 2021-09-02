import os

path = os.path.join("folder1", "folder2", "folder3", "file.png")
print(path)
print(os.sep) #koi znaci se koristat za razdeluvanje na pat
print(os.getcwd()) #get current working dir

os.chdir("C:\\")  # change working directory
os.chdir("D:\\Documents\\Py")
print(os.path.abspath("test.png"))
print(os.path.abspath("..\\..\\test.png"))

print(os.path.isabs("..\\..\\spam.png"))
print(os.path.isabs("D:\\folder1\\maja.png"))