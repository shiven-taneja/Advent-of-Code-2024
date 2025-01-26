if __name__ == '__main__':
    file = open('Day 3/input.txt')

    #Part 1 
    sum_of_muls = 0
    for f in file.readlines():
        f_s = f.split("mul(")[1:]
        for s in f_s:
            if "," in s:
                s = s.split(',')
            else: 
                continue
            num1 = s[0]
            brack = s[1].find(")")
            if brack in [1, 2, 3]:
                num2 = s[1][:brack]
            else:
                continue
            if num1.isdigit() and num2.isdigit():
                sum_of_muls += int(num1) * int(num2)
    print(sum_of_muls)

    
    # Part 2
    file = open('Day 3/input.txt') 
    sum_of_muls = 0
    do = True
    for f in file.readlines():
        for i in range(len(f)-11):
            if f[i:i+7] == 'don\'t()':
                do = False
            elif f[i:i+4] == "do()":
                do = True
            if do:
                if f[i:i+4] == "mul(":
                    s = f[i+4:i+12]
                    if "," in s:
                        s = s.split(',')
                    else: 
                        continue
                    num1 = s[0]
                    brack = s[1].find(")")
                    if brack in [1, 2, 3]:
                        num2 = s[1][:brack]
                    else:
                        continue
                    if num1.isdigit() and num2.isdigit():
                        sum_of_muls += int(num1) * int(num2)
    print(sum_of_muls)

