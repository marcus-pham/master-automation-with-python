import glob
import os
import shutil

source_dir = r'C:\mawp'

def list_all_file_in_directory(source_dir=source_dir):
	files = []
	for r, d, f in os.walk(source_dir):
		for file in f:
			if ('.py' in file) | ('.md' in file):
				print(file)


def copy_all_file_with_extension():
	# copy file with extension from a source directory
	files = glob.glob(os.path.join(source_dir, "*.md"))
	for file in files:
		if os.path.isfile(file):
			print(file)
			# shutil.copy2(file, dest_dir)

list_all_file_in_directory(source_dir)