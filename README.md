# remove_lines_by_indexes_from_file
It removes lines from a file by index. 
This code took a simple task and somehow made it complicated.

## What it does well
- Removes lines by overwriting files rather than copying/replacing/renaming them
- Memory efficient
- Good for massive files
- Loads files in chunks

## Setup
There is none. Just import the code file like:
> from remove_lines_by_indexes_from_file import *
and then use it as below.

## Usage
I left a test.txt file in the repository. Executing the following code will remove every other line:
> remove_lines_by_indexes_from_file('test.txt', [1, 3, 5, 7])
The first parameter is the filepath, and second parameter are the list line indexes to be removed.

## Note
buffer_size may be adjusted for speed vs memory usage.
