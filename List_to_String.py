def toString(arr):
    s = ''
    for i in range(len(arr)):
        if i > 0:
            if i == len(arr) - 1:
                # last one
                s = s + ' and '
            else:
                # second, third, ...
                s = s + ', '
        s = s + arr[i]
    return s

spam = ['apples', 'bananas', 'tofu', 'cats']
s=toString(spam)
print(s)