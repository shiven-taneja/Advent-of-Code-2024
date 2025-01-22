if __name__ == '__main__':
    file = open('Day 1/input.txt').readlines()
    
    #Part 1
    l1 = []
    l2 = []
    for f in file:
        splits = f.strip().split("   ")
        l1.append(int(splits[0]))
        l2.append(int(splits[1]))
    l1.sort()
    l2.sort()
    sum_of_dif = 0
    for i in range(len(l1)):
        sum_of_dif += abs(l1[i] - l2[i])
    print("Total distance between lists is", sum_of_dif)

    #Part 2
    sim_score = 0
    s1 = set(l1)
    for j in s1: 
        sim_score += j * l2.count(j)
    print("Similarity score between the lists is", sim_score)
