import os


def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


current_path()

"""
For Changing the current working directory
"""
os.chdir('../../')
# current_path()

"""
For getting the current working directory
"""
cwd = os.getcwd()
print("Current working directory:", cwd)

"""
For Making new directory
"""
directory = "Python_Go_Through"
parent_dir = "/"
path = os.path.join(parent_dir, directory)
# print(os.mkdir(path))
"""
os.listdir() method in Python is used to get the list of all files and directories in the specified directory. 
"""
path = "/files"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)

"""
For deleting the files  in the specified directory
"""
file = 'file1.txt'
location = "/Users/abdulrehman/PycharmProjects/Python_Go_Through/files"
path = os.path.join(location, file)
# os.remove(path)


"""
For deleting any directory in the specified directory
"""
directory = "file2"
parent = "/Users/abdulrehman/PycharmProjects/Python_Go_Through/files"
path = os.path.join(parent, directory)
# os.rmdir(path)
