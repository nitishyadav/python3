import tarfile
import shutil
import sys

shutil.make_archive('work_sample', 'gztar', root_dir='..', base_dir='/Users/nitish.yadav/Documents/python3',)
print("Archive contents:")
with tarfile.open('work_sample.tar.gz', 'r')as t_file:
	for names in t_file.getnames():
		print(names)
