# Short description

Yield successive n-sized chunks from list.

## Installing
```
pip install git+https://github.com/fchrulk/chunks
```

## Example use
```
from chunks.chunks import chunkList

my_list = ['a','b','c','d','e','f','g','h','i','j']
print(chunkList(l=my_list, n=2))
```
Output:
```
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j']]
```
