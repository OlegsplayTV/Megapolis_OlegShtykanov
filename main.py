# import csv

f = open('scientist.txt', encoding='UTF-8')
file = []
for line in f.readlines():
    line = line.split('#')
    #print(line)
    file.append(line)

chemicals = []
for line in file:
    if not line[1] in chemicals:
        chemicals.append(line[1])

#print(chemicals)
origfile = open('scientist_origin.txt', 'w', encoding='UTF-8')


true_chemicals = []
count = 0
for chemical in chemicals:
    minyear = 10 ** 10
    for iline in range(1, len(file)):
        line = file[iline]
        if line[1] == chemical:
            if int(line[2][:4]) < minyear:
                # print(line[2][:4])
                minyear = int(line[2][:4])
                count = iline
    true_chemicals.append(file[count])
    # line_to_orig = f'{str(file[count])[2:-4]}\n'
    # origfile.write(line_to_orig)

#print(true_chemicals)
schet = 0
chemicaltemp = []
while schet < len(true_chemicals)-2:
    schet = 0
    for ichemical in range(1, len(true_chemicals)-1):
        chemical = true_chemicals[ichemical]

        if int(str(chemical[2])[0:4]) > int(str(true_chemicals[ichemical+1][2])[0:4]):
            chemicaltemp = true_chemicals[ichemical]
            true_chemicals[ichemical] = true_chemicals[ichemical + 1]
            true_chemicals[ichemical + 1] = chemicaltemp

        else:
            schet += 1
print(true_chemicals)





# print(ascii('в'))