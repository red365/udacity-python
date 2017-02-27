# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(sym_list):
    # Your code here

    # Check for empty list
    if sym_list == []:
        return True

    # Create list of columns
    sym = convert_columns(sym_list)

    # Compare rows with columns
    if sym_list == sym:
        return True
    else:
        return False

def convert_columns(sym_list):
    x = 0
    y = 0
    columns = []
    for row in sym_list:
        no_of_columns = len(row)
    while x < no_of_columns:
        column = [] 
        while y < len(sym_list):
            column.append(sym_list[y][x])
            y += 1
        x += 1
        y = 0
        columns.append(column)
    return columns



print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

 

