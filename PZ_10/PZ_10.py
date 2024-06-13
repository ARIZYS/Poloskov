#В N нескольких колхозах выращивают некоторые сельскохозяйственные культуры из имеющегося
#перечня. Определить культуры, выращиваемые во всех колхозах, и культуры,
#выращиваемые только в некоторых из них.


zemskiy = {'ячмень', 'гречиха'}
voronskiy = {'ячмень','подсолнечник','овёс'}
kleevskiy = {'ячмень','подсолнечник'}

All_C = (zemskiy & voronskiy & kleevskiy)

for i in zemskiy:
    if i not in voronskiy and i not in kleevskiy:
        zemskiy_1 = i
        print('Культура выриваемая только в zemskyi:',zemskiy_1)

for i in voronskiy:
    if i not in zemskiy and i not in kleevskiy:
        voronskiy_1 = i
        print('Культура выриваемая только в voronskiy:', voronskiy_1)

for i in kleevskiy:
    if i not in voronskiy and i not in zemskiy:
        kleevskiy_1 = i
        print('Культура выриваемая только в kleevskiy:',kleevskiy_1)
else:
    print("Культура выриваемая только в kleevskiy: Нет индивидуальных элементов")

print("Культуры, выращиваемые во всех колхозах:", All_C)