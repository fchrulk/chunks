# Short description

Dividing list or dataframe into n-sized chunks.

## Installing
```
pip install git+https://github.com/fchrulk/chunks
```

## Example use
```
from chunks.chunks import chunks

my_list = ['a','b','c','d','e','f','g','h','i','j']
my_list_chunked = chunks(l=my_list, n=2)
print(my_list_chunked)
```
Output:
```
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j']]
```
