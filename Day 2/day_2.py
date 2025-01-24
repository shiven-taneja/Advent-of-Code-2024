if __name__ == '__main__':
    file = open('Day 2/input.txt').readlines()
    reports = [f.strip().split(" ") for f in file]

    def check_unsafe(levels):
    
        if len(levels) <= 1:
            return True, -1

        first_dif = int(levels[1]) - int(levels[0])
        if first_dif == 0 or abs(first_dif) > 3:
            return False, 1
        
        inc = first_dif > 0
        for i in range(2, len(levels)):
            dif = int(levels[i]) - int(levels[i - 1])
            if dif == 0 or abs(dif) > 3:
                return False, i
            if (inc and dif < 0) or (not inc and dif > 0):
                return False, i
        return True, -1
        

    #Part 1 
    safe = 0
    for levels in reports:
        safe_checked, _ = check_unsafe(levels)
        if safe_checked:
            safe += 1
        
    print("Number of safe reports:", safe)

    #TODO
    #Part 2
    safe = 0
    for levels in reports:
        safe_checked, ind = check_unsafe(levels)
        if safe_checked:
            safe += 1
        else:
            # Try removing one level and check again
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i + 1:]
                if check_unsafe(new_levels)[0]:
                    safe += 1
                    break
    print("Number of safe reports (w/ dampner):", safe)