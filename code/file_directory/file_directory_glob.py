# understand glob
import os
import glob
import shutil

root = r'C:\mawp\code\file_directory\root'

def understand_glob(root):
	# search all .txt file under root only
	txt_files_no_recursive = glob.glob(os.path.join(root, '*.txt'))
	print(txt_files_no_recursive)

	# search all file .txt under root recursively
	txt_files_recursive = glob.glob(os.path.join(root, '**/*.txt'), recursive=True)
	print(txt_files_recursive)

	# search all file and directory under root recursively
	files_dirs_recursive = glob.glob(os.path.join(root, '**'), recursive=True)
	print(files_dirs_recursive)


def list_all_file_in_directory(root):
	'''
		Do search recursively inside directory
	'''
	files_dirs = glob.glob(os.path.join(root, '**'), recursive=True)
	# print(files_dirs)

	for item in files_dirs:
		if os.path.isfile(item):
			print(item)


def copy_all_files_with_extension(source, destination, extension):
	'''
		Do search recursively inside directory
	'''
	files_dirs = glob.glob(os.path.join(root, '**'), recursive=True)
	for item in files_dirs:
		if os.path.isfile(item):
			if item.endswith(extension):
				print(item)
				shutil.copy(item, destination)



understand_glob(root)

list_all_file_in_directory(root)

source = r'C:\mawp\code\file_directory\root'
destination = r'C:\mawp\code\file_directory\destination'
copy_all_files_with_extension(source, destination, '.txt')