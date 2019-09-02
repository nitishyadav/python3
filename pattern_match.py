#Python has the 'glob' module, which is used to find the names of files and directories that match specific patterns
import glob
file_match = glob.glob("*.txt")
print(file_match)
file_match = glob.glob("[0-9].txt")
print(file_match)
file_match = glob.glob("**/*.txt",recursive=True)
print(file_match)
file_match = glob.glob("**/",recursive=True)
print(file_match)
