from random import randrange

mat = []
question = input("If you like to input your own matrix please input Y otherwise you will see the example:\n")
if question == "Y":
    while True:
        try:
            size = int(input('Please input the matrix length:\n'))
            break
        except:
            print("Incorrect input value. Please input only number\n")
    print("Please input the elements of matrix:\n")

    for i in range(size):
        tmp = []
        for j in range(size):
            value = input()
            if value or value == 0:
                tmp.append(value)
            else:
                tmp.append(0)
        mat.append(tmp)
else:
    size = 5
    mat = [[randrange(99) for x in range(size)] for y in range(size)]
print("")


def rotate_matrix(matrix):
    for x in range(0, int(size / 2)):
        for y in range(x, size - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][size - 1 - x]
            matrix[y][size - 1 - x] = matrix[size - 1 - x][size - 1 - y]
            matrix[size - 1 - x][size - 1 - y] = matrix[size - 1 - y][x]
            matrix[size - 1 - y][x] = temp


def show_matrix(matrix):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=' ')
        print("")
    print("")


print("THIS IS A YOUR MATRIX:\n")
show_matrix(mat)

rotate_matrix(mat)

print("THIS IS A ROTATED MATRIX:\n")
show_matrix(mat)
