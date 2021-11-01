def color(x,y):
    result = []
    for m in range(0,x):
        temp = []
        for e in range(0,y):
            temp.append((m+e) % 2)
        result.append(temp)
    return result


ez2c = (color(2,2))


for row in ez2c:
    print(row)