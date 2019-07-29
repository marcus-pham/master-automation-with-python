Normally to working with file system in python we use following package 

### Objectives

Copy all ".txt" files recursively. For easy of demo, support we have following structure of folder and file.

inside `source` are 3 levels of folder 1,2,3. In each folder has one `txt` file with name same with folder name.

![](images/2019-07-29_10-34-56.png)



#### Use os.path.join



#### Use glob.glob

Glob work base on pattern. 

* '*' replace for any string
* '?' replace for any character

##### Search Use Wildcards at One Level

To search all `.txt` file right under `source` folder, we use pattern `*.txt`

```python
# search only right inside root
pattern = '*.txt'

# joint to create absolute path
absolute_pattern = os.path.join('source', pattern)
result = glob.glob(absolute_pattern)
print(result)
```

Result will have only file `1.txt`

```python
"""
['source\\1.txt']
"""
```

##### Search Use Wildcards at All Level

To search all `.txt` file under all folder level, we use pattern `**\*.txt`

`**` tell to glob that we want to search recursively.

And we also need to specify parameter `recursive=True`. Following coding will search for '.txt' file in all directory level.

```python
# recursive pattern
pattern = '**\*.txt'

absolute_pattern = os.path.join('source', pattern)
result = glob.glob(absolute_pattern, recursive=True)
print(result)
```

Print out result

```python
'''
['source\\1.txt', 'source\\1\\2.txt', 'source\\1\\2\\3.txt']
'''
```

##### Copy all ".txt" Files Recursively

Now we already know how to search for all `.txt` file. To copy a file to directory, we use function `copy` inside `shutil` package. That it, mission accomplished.

```python
def copy_files_with_extension(source, destination, extension):
	pattern = os.path.join(source,'**\*.{0}'.format(extension))
	files = glob.glob(pattern, recursive=True)

	for file in files:
		shutil.copy(file, destination)

copy_files_with_extension('source', 'destination', 'txt')
```

After running, inside `destination` will have copied file.

![](images/2019-07-29_14-22-30.png)

#### Use os.walk





