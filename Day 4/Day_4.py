def xmas_forward(file, i, j):
    if j + 3 <= len(file[i]):
        if file[i][j+1] == 'M' and file[i][j+2] == 'A' and file[i][j+3] == "S":
            return 1 
    return 0

def xmas_backward(file, i, j):
    if j >= 3:
        if file[i][j-1] == 'M' and file[i][j-2] == 'A' and file[i][j-3] == "S":
            return 1
    return 0

def xmas_up(file, i, j):
    if i >= 3:
        if file[i-1][j] == 'M' and file[i-2][j] == 'A' and file[i-3][j] == "S":
            return 1
    return 0

def xmas_down(file, i, j):
    if i + 3 < len(file):
        if file[i+1][j] == 'M' and file[i+2][j] == 'A' and file[i+3][j] == "S":
            return 1
    return 0

def xmas_diag(file, i, j):
    c = 0
    #diag right down
    if i + 3 < len(file) and j + 3 <= len(file[i]):
        if file[i+1][j+1] == 'M' and file[i+2][j+2] == 'A' and file[i+3][j+3] == "S":
            c += 1
    #diag left down
    if i + 3 < len(file) and j >= 3:
        if file[i+1][j-1] == 'M' and file[i+2][j-2] == 'A' and file[i+3][j-3] == "S":
            c += 1

    #diag right up
    if i >= 3 and j + 3 <= len(file[i]):
        if file[i-1][j+1] == 'M' and file[i-2][j+2] == 'A' and file[i-3][j+3] == "S":
            c += 1
    #diag left up
    if i >= 3 and j >= 3:
        if file[i-1][j-1] == 'M' and file[i-2][j-2] == 'A' and file[i-3][j-3] == "S":
            c += 1
            
    return c


if __name__ == '__main__':

    # Part 1 
    file = open("Day 4/input.txt").readlines()
    count = 0
    for i in range(len(file)): 
        for j in range(len(file[i])):
            if file[i][j] == 'X':
                count += xmas_forward(file, i, j) 
                count += xmas_backward(file, i, j)
                count += xmas_up(file, i, j)
                count += xmas_down(file, i, j)
                count += xmas_diag(file, i, j)
    print(count)
                
    #Part 2 
    count = 0
    for i in range(1, len(file) - 1):
        for j in range(1, len(file[i])-1):
            if file[i][j] == "A":
                if ((file[i-1][j-1] == "M" and file[i+1][j+1] == "S") or (file[i-1][j-1] == "S" and file[i+1][j+1] == "M")) and ((file[i+1][j-1] == "M" and file[i-1][j+1] == "S") or (file[i+1][j-1] == "S" and file[i-1][j+1] == "M")):
                    count += 1
    print(count)