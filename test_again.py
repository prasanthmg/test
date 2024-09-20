d  = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500
}

RN = ['CLXXXIX', 'CD', 'XL', 'XIX']
temp_RN = []
for rn in RN:
    decimal = 0
    if len(rn)==2:
        if d[rn[0]] < d[rn[1]]:
            decimal = d[rn[1]] - d[rn[0]]
            temp_RN.append(decimal)
            continue
    i = 0
    while i < len(rn):
        if (i<(len(rn)-1)) and (d[rn[i]] < d[rn[i+1]]):
            decimal += d[rn[i+1]] - d[rn[i]]
            i+=2
        else:
            decimal += d[rn[i]]
            i+=1
    while i < len(rn)-1:
        if (d[rn[i]] < d[rn[i+1]]):
            decimal -= d[rn[i]]
        else:
            decimal += d[rn[i]]
        i+=1
    decimal += d[rn[-1]]
    temp_RN.append(decimal)
RN = temp_RN
print(RN)
