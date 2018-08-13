def pascal_triangle(step=None):
    t_row = [1]
    curr = [0]
    i = 1
    for i in range(max(step, 0)):
        t_row = [(i + j) for i, j in zip(t_row+curr, curr+t_row)]
        print(t_row)
    return step >= 1

if __name__ == '__main__':
    pascal_triangle(5)