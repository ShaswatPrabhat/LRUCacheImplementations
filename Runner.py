from LRUOrderedDict import LRUOrderedDict

if __name__ == '__main__':
    d = LRUOrderedDict.LRUCache(3)
    d.put('a', 'a')
    d.put('b', 'b')
    d.put('c', 'c')
    d.get('a')
    d.put('d', 'd')
    print(d.cache)
