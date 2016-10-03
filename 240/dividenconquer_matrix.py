matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30],
  [19, 22, 24, 27, 31]
]

matrix = [[1,3,5]]

def get_topright(matrix):
    m = len(matrix)
    n = len(matrix[0])

    # print matrix[0:m/2]
    return [row[n/2:n] for row in matrix[0:m/2]]

def get_topright_center(matrix):
    m = len(matrix)
    n = len(matrix[0])

    i = 0
    ii = m/2
    j = n/2
    jj = n

    return matrix[i + (ii-i)/2][j + (jj-j)/2]

def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

if __name__=="__main__":

    print_matrix(matrix)
    print " ----- "
    print_matrix(get_topright(matrix))
    print " ----- "
    print get_topright_center(matrix)