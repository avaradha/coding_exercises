def steps(num=None):
    for i in (range(1, num + 1, 1)):
        print('#' * i + ' '* (num - i))

if __name__ == '__main__':
    steps(10)