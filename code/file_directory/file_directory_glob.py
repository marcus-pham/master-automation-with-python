# scenario
import glob
import os
import shutil

# understand glob
root = r'C:\mawp\code\file_directory\root'

def understand_glob(root):
	# search all file under root only
	print(glob.glob(os.path.join(root, '*.*')))

	# search all file and directory under root recursively
	print(glob.glob(os.path.join(root, '**'), recursive=True))


understand_glob(root)


def list_all_file_in_directory(root):
	files_dirs = glob.glob(os.path.join(root, '**'), recursive=True)
	print(files_dirs)

	for item in files_dirs:
		if os.path.isfile(item)