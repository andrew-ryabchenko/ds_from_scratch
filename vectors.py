height_weight_age = [70, # inches,
                    170, # pounds,
                    40 ] # years

grades = [95, # exam1
            80, # exam2
            75, # exam3
            62 ] # exam4

matrix=[[1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10]]
# Define function to add and subtract vectors element-wise

def vector_add(v,w):
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_sub(v,w):
    return [v_i - w_i for v_i,w_i in zip(v,w)]

# Define function to add multiple vectors

def vector_sum(vectors):
    result = vectors[0]
    for vect in vectors[1:]:
        result = vector_add(result, vect)
    return result

#print(vector_sum(matrix))

from functools import reduce, partial

#vector_sum=reduce(vector_add, matrix)

# We predefine one of the arguments of the reduce function while other one will be passed to the new 
# vector_sum function

vector_sum = partial(reduce, vector_add)
print(vector_sum(matrix))

# Define function to multiply vector by scalar

def scalar_mult(c,v):
    return [c*v_i for v_i in v]

# Define function to compute element-wise mean of multiple vectors

def vector_mean(vectors):
    # Vector count
    count=len(vectors)
    return scalar_mult(1/count, vector_sum(vectors))

#print(vector_mean(matrix))

# Calculate dot product of two vectors.
# Dot product is the sum of the element-wise vectors product

def dot(v,w):
    return sum([v_i*w_i for v_i,w_i in zip(v,w)])

print(dot(matrix[0], matrix[0]))