# Работа с файлами на Python
import os.path
check_file = os.path.isfile(r'D:\\Python.All\\Py.projects\\Laba_3.txt')
if check_file == 0:
    f = open(r'D:\\Python.All\\Py.projects\\Laba_3.txt', mode='w')
    f.close()
    f = open(r'D:\\Python.All\\Py.projects\\Laba_3.txt', mode='a+')
    Flag = '  \n'\
           'ДОБЫЧА НЕФТИ И ГАЗА НА РОССИЙСКОМ ШЕЛЬФЕ \n ' \
           'Проект «Сахалин- 1» В 2019 году продолжена эффективная реализация проекта «Сахалин-1». \n ' \
           'ПАО «НК «Роснефть» является участником проекта в составе консорциума, в состав которого \n' \
           ' входят компании ExxonMobil (США), SODECO (Япония), ONGC Videsh Ltd. (Индия). Доля Компании \n' \
           'в проекте – 20 %, оператор проекта – компания «Эксон Нефтегаз Лимитед».\n ' \
           'В рамках проекта«Сахалин-1»идет добыча углеводородов на четырех морских месторождениях: Чайво, \n' \
           ' Одопту-море, Лебединское (в границах лицензионного участка Одопту) и Аркутун-Даги, расположенных \n' \
           'в акватории Охотского моря на северо-восточном шельфе о. Сахалин. \n ' \
           'Разработка месторождений проекта (Чайво, Одопту-море, Лебединское и Аркутун-Даги) осуществляется с\n' \
           ' применением самых современных технологий и методов организации работ. Добыча нефти на месторождении\n' \
           ' Одопту-море осуществляется с береговой площадки с помощью горизонтальных скважин со сверхдальним отходом \n' \
           'от вертикали; на месторождении Чайво – с береговой площадки и с платформы «Орлан» скважинами рекордной \n' \
           'протяженности по стволу; на месторождении Аркутун-Даги – с крупнейшей в мире по весу верхней части морской\n' \
           ' стационарной платформы «Беркут». \n' \
           ' В 2019 году достигнут рекорд по добыче нефти и конденсата: в целом по проекту\n' \
           ' «Сахалин-1» добыто нефти и конденсата 13,0 млн т (доля «Роснефти» составила 2,6 млн т). Потребителям \n' \
           'поставлено почти 2,4 млрд куб. м газа (доля «Роснефти» составила 0,5 млрд куб. м).'
    f.write(Flag)
    f.close()
    f = open(r'D:\\Python.All\\Py.projects\\Laba_3.txt', mode='r')

    f.close()
else:
    f = open(r'D:\\Python.All\\Py.projects\\Laba_3.txt', mode='r')
    n = int(input('enter the order of the number \n'))
    s2 = f.readline()
    for s2 in f:

        s1 = s2.split()

        first = 10 ** n
        second = first * 10
        Arr3 = []
        for i in range(0, len(s1)):
            s = s1[i]
            if ord(s[0]) >= 48 and ord(s[0]) <= 57:
                Arr = ''
                Arr2 = ''
                status = 0
                for y in range(0, len(s)):

                    if ord(s[y]) == 44:
                        status += 1
                    if ord(s[y]) >= 48 and ord(s[y]) <= 57:
                        if status == 0:
                            Arr += s[y]
                        else:
                            Arr2 += s[y]
                asd = len(Arr2)
                stroka = Arr + ',' + Arr2
                if int(Arr) >= first and int(Arr) <= second:
                    s1[i] = ' '
                else:
                    Arr3.append(stroka)
                #print(stroka)
        print(' '.join(s1))

# f.close()
