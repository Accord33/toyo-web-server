one = {1:1,2:2,3:3,4:4,5:5}
two = 0


for i in one:
    two += 1
    
    if two > 4:
        break
    print(one[i])