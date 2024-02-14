f = open('scientist.txt', encoding='UTF-8') # открытие основного файла
file = [] # список для данных из файла

for line in f.readlines(): # Каждая строка превращается в массив, добавляется в file
    line = line.split('#')
    # print(line)
    file.append(line)

chemicals = [] # список неповторяющихся лекарств (СНЛ)
for line in file: # заполнение СНЛ
    if not line[1] in chemicals:
        chemicals.append(line[1])

# цикл для настоящих создателей лекарств - true_chemicals (он указан далее):
true_chemicals = [] # список для настоящих создателей лекарств
count = 0 # Счётчик для следующего цикла
for chemical in chemicals: # просмотр и поиск "полекарственно"
    minyear = 10 ** 10 # Минимальная дата (обновляется далее)
    for iline in range(1, len(file)): # поиск лекарства в каждой строке
        line = file[iline]
        if line[1] == chemical:
            if int(line[2][:4]) < minyear: # для поиска минимальной даты появления лекраства
                # print(line[2][:4])
                minyear = int(line[2][:4])
                count = iline
    true_chemicals.append(file[count])


# Цикл для true_chemicals (сортировка):
schet = 0
chemicaltemp = []
while schet < len(true_chemicals) - 2:
    schet = 0 # Переменная для узнавания правильности сортировки
    for ichemical in range(1, len(true_chemicals) - 1):
        chemical = true_chemicals[ichemical]

        if int(str(chemical[2])[0:4]) > int(str(true_chemicals[ichemical + 1][2])[0:4]):
            chemicaltemp = true_chemicals[ichemical]
            true_chemicals[ichemical] = true_chemicals[ichemical + 1]
            true_chemicals[ichemical + 1] = chemicaltemp

        else:
            schet += 1

# Создание и открытие файла для записи оригинальных создателей
origfile = open('scientist_origin.txt', 'w', encoding='UTF-8')
for Scientist in range(len(true_chemicals)):
    # Scientist = f"{str(true_chemicals[Scientist])[1:-4]}'\n"
    Scientist = f"{true_chemicals[Scientist][0]}, " \
                f"{true_chemicals[Scientist][1]}, {true_chemicals[Scientist][2]}, {true_chemicals[Scientist][3]}"
    origfile.write(Scientist)

#
allopyrinol = []
for line in file:
    if line[1] == 'Аллопуринол':
        allopyrinol.append(line)

# Разработчики Аллопуринола:
print('Разработчиками Аллопуринола были такие люди:')
schet2 = 0
whoyearmax = 0
while schet2 < len(allopyrinol) - 2:
    for who in range(len(allopyrinol)):
        if int(str(who[2])[0:4]) > int(str(true_chemicals[who + 1][2])[0:4]):
            print(f'{who[0]} - {who[1]}')

# print(ascii('в'))
