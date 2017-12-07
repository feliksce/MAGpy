g = 4
r = 4

# TODO: need names for each irrep

# fill in with ones
characters = [1 for each in range(r)]

# check if sum of characters is equal to g
squared = 0
temp = 1
temp2 = 1
while not squared == g:

    squared = sum([each ** 2 for each in characters])
    if squared == g: print(characters); print("End"); break
    elif squared < g:
        # enumerates (from the back) numbers in characters array
        if temp < r:
            characters[-temp] += 1
            temp += 1
        else:
            temp = 1
    # checks for squared being less than g
    elif squared > g:
        if temp2 < r:
            characters[temp2] -= 1
            temp2 += 1
        else:
            temp2 = 1
else:
    print("go")
