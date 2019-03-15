def chunks(l, n, N=None):
    """
    Dividing list or dataframe intp n-sized chunks.
    l = your_list
    N = define size
    n = define size of each chunk

    Example:
    my_list = ['a','b','c','d','e','f','g','h','i','j']
    chunked_list = chunks(l=my_list, n=2)
    print(chunked_list)
    
    my_list = ['a','b','c','d','e','f','g','h','i','j']
    chunked_list = chunks(l=my_list, N=2)
    print(chunked_list)
    
    
    Output:
    [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j']]
    [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']]
    """
    new = []
    if (N is not None):
        for i in range(0, len(l), N):    
            new.append(l[i:i + N])
    else:
        for i in range(0, len(l), n):    
            new.append(l[i:i + n])
    return new
