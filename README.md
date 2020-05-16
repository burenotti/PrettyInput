# PrettyInput
This package is needed to simplify input from streams.
## Why?
Sometimes you need to input some numbers from file or command line.
It will be okay if the numbers were written one in a row.
file content:
```
12
12.3
45
-34
```
Then you can use this simple code:
```python
...
for line in file:
  number = float(line.strip())
  ...
```
But if the numbers has been put in a one row. You have to write something like this
```python
numbers = list(map(int, input().split()))
```
I wanted to make library via using which you wouldn't care about this two cases.

## Instalation
```bash
pip install prettyinput
```

## Using
You have two ways to use this library:
- Use row functions
- Use StreamIO class

There are 3 functions now:
- read_int() - read int
- read_float(allow_exp=True) - read float (if allow exp is True you can read numbers in exponential form).
- read_str() - read str till stop char

Functions has same argument: stream (default stream=stdin) a stream you want to use to input
example:
```python
x = read_int() # read int form stdin (command line)

#from file:
f = open('file.txt', 'r')
x = read_int(stream=f)
```
But it is not comfortable to write stream every time when you read from file.
So You can use StreamIO.

```python
#first you should create object:
stream = StreamIO(stream=sys.stdin) #from sys.stdin or already opened file
stream = StreamIO.from_file(filepath, mode) # from file
#then you can use same functions
stream.read_int()
stream.read_float()
stream.close()
```
