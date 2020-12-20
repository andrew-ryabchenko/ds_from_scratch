# A matrix is a two-dimensional collection of numbers where
# rows are lists of the same lenght

A = [[1, 2, 3], # A has 2 rows and 3 columns
    [4, 5, 6]]

B = [[1, 2], # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

# Function that determines the shape of a matrix

def shape(matrix):
    return (len(matrix), len(matrix[0]))

# Function that creates matrix of a given shape and fills it with output of entry_fn

def make_matrix(nrows, ncols, entry_fn):
    return [ [entry_fn(i,j,nrows) for j in range(ncols)] for i in range(nrows) ]

# Make entry_fn for creation of a diagonal matrix
f = lambda i,j,nrows: 0 if (i+j+1==nrows or i==j) else 3

matrix = make_matrix(10,10,f)
for i in range(len(matrix)):
    print(matrix[i])