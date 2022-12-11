import math
import random

def fillArray() -> list:
    number = int(input('Введите длину массива: '))
    min = int(input('Введите минимальное число рандомайзера: '))
    max = int(input('Введите максимальное число рандомайзера: '))
    list = []
    for i in range(number):
        list.append(random.randint(min, max))
    print('array: ',list)
    return list

def fillFiles(array1, array2):
    path1 = 'file ex5_1.txt'
    path2 = 'file ex5_2.txt'
    data1 = open(path1, 'a')
    data2 = open(path2, 'a')
    open(path1, 'w').close()
    open(path2, 'w').close()
    data1.write(str(array1))
    data2.write(str(array2))
    data1.close()
    data2.close()

def ex1():
    number = int(input('Введите число округления: '))
    pi = math.pi
    print('Число пи было округлено: ', round(pi, number))

def ex2():
    num = int(input("Введите число: "))
    i = 2 # первое простое число
    array = []
    old = num
    while i <= num:
        if num % i == 0:
            array.append(i)
            num //= i
            #print(i, ' ', num)
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {array}")

def ex3(array) -> list:
    list1 = []
    for i in range(len(array)):
        if array[i] not in list1:
            list1.append(array[i])
    return list1

def ex4(array):
    string = ''
    path = 'file ex4.txt'
    data = open(path, 'a')
    open(path, 'w').close()
    for i in range(len(array)):
        string = string + str(array[i]) + '*x^' + str(len(array)- 1 - i) + ' + '
    string = string.replace('^1', '')
    string = string.replace('*x^0 +', '')
    print(string)
    data.write(string)
    data.close()

def ex5():
    path1 = 'file ex5_1.txt'
    path2 = 'file ex5_2.txt'
    data1 = open(path1, 'r')
    data2 = open(path2, 'r')
    array1 = []
    array2 = []
    summaryArray = []
    string1 = data1.read()
    string2 = data2.read()
    data1.close()
    data2.close()
    string1 = string1.replace('[','')
    string1 = string1.replace(']','')
    string1 = string1.replace(' ','')
    string2 = string2.replace('[','')
    string2 = string2.replace(']','')
    string2 = string2.replace(' ','')
    array1 = string1.split(',')
    array2 = string2.split(',')
    for i in range(len(array1)):
        array1[i] = int(array1[i])
    for i in range(len(array2)):
        array2[i] = int(array2[i])
    lenght1 = len(array1)
    lenght2 = len(array2)
    print('arr1 ',array1)
    print('arr2 ',array2)
    arrayOfIndex = []

    if lenght1 == lenght2:
        for i in range(lenght1):
            summaryArray.append(array1[i] + array2[i])
    elif lenght1 < lenght2:
        for i in range(lenght1):
            k = -1 - i
            a = array1[k]
            b = array2[k]
            print('i: ',i, 'k: ',k,'a: ',a, 'b: ' ,b, 'sum: ', a+b)
            summaryArray.append(a + b)
            arrayOfIndex.append(lenght2 - i)
    else: 
        for i in range(lenght2):
            k = -1 - i
            a = array1[k]
            b = array2[k]
            print('i: ',i, 'k: ',k,'a: ',a, 'b: ' ,b, 'sum: ', a+b)
            summaryArray.append(a + b)
            arrayOfIndex.append(lenght1 - i)

    summaryArray.reverse()

    if lenght1 == lenght2:
        summaryArray = summaryArray
    elif lenght1 < lenght2:
        for i in range(len(arrayOfIndex)):
            array2.pop(arrayOfIndex[i] - 1)
        summaryArray = array2 + summaryArray
    else:
        for i in range(len(arrayOfIndex)):
            array1.pop(arrayOfIndex[i] - 1)
        summaryArray = array1 + summaryArray
    print(summaryArray)
    print(arrayOfIndex)

    string = ''
    path = 'file ex5_resault.txt'
    dataRasult = open(path, 'a')
    open(path, 'w').close()
    for i in range(len(summaryArray)):
        string = string + str(summaryArray[i]) + '*x^' + str(len(summaryArray)- 1 - i) + ' + '
    string = string.replace('^1', '')
    string = string.replace('*x^0 +', '')
    print(string)
    dataRasult.write(string)
    dataRasult.close()

print('1. Вычислить число c заданной точностью d.')
print(ex1())
print('2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.')
print(ex2())
print('3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')
print(ex3(fillArray()))
print('4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.')
print(ex4(fillArray()))
print('5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.')
print(fillFiles(fillArray(),fillArray()))
print(ex5())