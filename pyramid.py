def pyramid(step=None):
    final_row = (2 * step) - 1
    if step == 1:
        print('#')
    else:
        for i in range(step, 0 , -1):
            tot_col = ((2 * i) - 1)
            space_count = tot_col // 2
            hash_count = final_row - (space_count * 2)
            print(' ' * space_count + '#' * hash_count + ' ' * space_count)


if __name__ == '__main__':
    pyramid(1)
    pyramid(5)