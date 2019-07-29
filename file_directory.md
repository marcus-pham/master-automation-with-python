Automate manage file and directory in python.

### Objectives

* Copy all ".txt" files recursively

#### Use Glob

Glob work base on regular expression. For easy of demo, support we have following structure of folder and file.

inside `source` are 3 levels of folder 1,2,3. In each folder has one `txt` file with name same with folder name.

![](images/2019-07-29_10-34-56.png)

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

##### Task 1 : List all ".txt" Files Recursively



##### Task 2 : Copy all ".txt" Files Recursively



#### Walk

