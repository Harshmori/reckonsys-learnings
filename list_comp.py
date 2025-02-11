# problem 1 :

def flatt_mat(matrix):
    val = [num**2 for row in matrix for num in row if num%2==0]
    return val
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 

ans = flat_mat(matrix)
print(ans)


# problem 2


def flat_mat(pythonCopyEditwords):
    val = [word.upper() for row in pythonCopyEditwords for word in row if len(word)>3]
    return val


pythonCopyEditwords = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]
 

ans = flat_mat(pythonCopyEditwords)
print(ans)



