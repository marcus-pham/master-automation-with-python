# scenario
# create markdown toc
# https://github.com/jonschlinkert/markdown-toc

import glob
import os
import shutil

# os.walk
# https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right
def understand_walk(root):
	path = next(os.walk(root))[0]
	print('path', path)

	folders_in_path = next(os.walk(root))[1]
	print('folders_in_path', folders_in_path)

	files_in_path = next(os.walk(root))[2]
	print('files_in_path', files_in_path)

def understand_walk_with_for_loop(root):
	for path, folders_in_path, files_in_path in os.walk(root):
		print('path', path)
		print('folders_in_path', folders_in_path)
		print('files_in_path', files_in_path)
		print('\n')

def list_all_file_in_directory(root):
	for path, folders_in_path, files_in_path in os.walk(root):
		for file in files_in_path:
			print(file)

def copy_all_file_with_extension(source, destination, extension):
	for path, folders_in_path, files_in_path in os.walk(source):
		for file in files_in_path:
			if file.endswith(extension):
				print(file)
				shutil.copy(os.path.join(path,file), destination)


# root = r'C:\mawp\code\file_directory\root'
# understand_walk(root)
# understand_walk_with_for_loop(root)
# list_all_file_in_directory(root)


# source = r'C:\mawp\code\file_directory\root'
# destination = r'C:\mawp\code\file_directory\destination'
# copy_all_file_with_extension(source, destination, '.txt')



# understand glob
# https://pymotw.com/3/glob/
root = r'C:\mawp\code\file_directory\root'
def understand_glob(root):
	# search all file with extension txt
	print(glob.glob(os.path.join(root, '*.*')))

	# search all file and directory inside root recursively
	print(glob.glob(os.path.join(root, '**'), recursive=True))


understand_glob(root)

# def copy_all_file_with_extension(source, destination, extension):
# 	# copy file with extension from a source directory
# 	files = glob.glob(os.path.join(source_dir, "*.md"))
# 	for file in files:
# 		if os.path.isfile(file):
# 			print(file)
# 			# shutil.copy2(file, dest_dir)