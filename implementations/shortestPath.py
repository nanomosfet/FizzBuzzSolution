def shortestCommonPath(arr):
    shortest = None
    for path in arr:
        if shortest == None:
            shortest = path.split('/')[1:]    
        else:
            path = path.split('/')[1:]
            if len(shortest) > len(path):
                shortest = path

    print(shortest)
    for path in arr[1:]:
        pathArr = path.split('/')[1:]
        for i in range(0, len(shortest)):
            if shortest[i] != pathArr[i]:
                shortest = shortest[:i]
                break



    res = '/'+'/'.join(shortest)
    return res




arr1 = ['/usr/bin/python', '/usr/local/python', '/usr/local/bin/python']
arr2 = ['/var/', '/', '/']
arr3 = ['/var/lib/docker', '/var/', '/']
arr4 = ['/', '/var/', '/']
arr5 = ['/', '/var/', '/somefile/']
arr6 = ['/abc/abc/123/abc/', '/abc/abc/123/', '/abc/abc/']

try:
    res = shortestCommonPath(arr1)
    assert res == '/usr'
except AssertionError as A:
    print('Failed test: your output = ' + res)

try:
    res = shortestCommonPath(arr2)
    assert res == '/'
except AssertionError as A:
    print('Failed test: your output = ' + res)

try:
    res = shortestCommonPath(arr3)
    assert res == '/'
except AssertionError as A:
    print('Failed test: your output = ' + res)


try:
    res = shortestCommonPath(arr4)
    assert res == '/'
except AssertionError as A:
    print('Failed test: your output = ' + res)

try:
    res = shortestCommonPath(arr5)
    assert res == '/'
except AssertionError as A:
    print('Failed test: your output = ' + res)

try:
    res = shortestCommonPath(arr6)
    assert res == '/abc/abc'
except AssertionError as A:
    print('Failed test: your output = ' + res)
# assert  == '/usr/'
# assert shortestCommonPath(arr2) == '/'
# assert shortestCommonPath(arr3) == '/'
# assert shortestCommonPath(arr4) == '/'
# assert shortestCommonPath(arr5) == '/'
# print(shortestCommonPath(arr6))