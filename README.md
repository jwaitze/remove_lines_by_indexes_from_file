# remove_lines_by_indexes_from_file
It removes lines from a file by index. 
This code took a simple task and somehow made it complicated.

## What it does well
- Removes lines by overwriting file rather than copying/replacing/renaming it
- Highly memory efficient
- Good for massive files

## Setup
There is none.

## Usage
I left a test.txt file in the repository. Executing the following code will remove every other line:
> remove_lines_by_indexes_from_file('test.txt', [1, 3, 5, 7])

## Note
buffer_size may be adjusted for speed vs memory usage.
