import numpy
import random
import time

def to_csv():
    with open("household.csv",'w+') as csv:
        with open("household_power_consumption.txt",'r') as txt:
            for i,string in enumerate(txt):
                if (i % 10) == 0:
                    if '?' not in string:
                        string = string.replace(";","/",1)
                        csv.write(string)


def get_array():
    name = ['D/T','GAP','GRP','V','GI','SM1','SM2','SM3']
    date_type = ['S16','f8','f8','f8','f8','f8','f8','f8']
    array = numpy.genfromtxt("household.csv",dtype=date_type,delimiter=";",skip_header=1,names=name)
    return array

def task1_numpy():
    start = time.time()
    array = get_array()
    array = array[numpy.where(array['GAP']>5)]
    print(array[0])
    end = time.time()
    print(end-start)

def task2_numpy():
    start = time.time()
    array = get_array()
    array = array[numpy.where(array["V"]>235)]
    print(array[0])
    end = time.time()
    print(end-start)

def task3_numpy():
    start = time.time()
    array = get_array()
    array = array[numpy.where(array["GI"]>19,array["GI"]<20,array["SM2"]>array["SM2"])]
    print(array[0])
    end = time.time()
    print(end-start)

def task4_numpy():
    start = time.time()
    array = get_array()
    mask = numpy.zeros(len(array),dtype=bool)
    K = 204923
    M = 5000
    for i,row in enumerate(array):
        if M/K >= random.random():
            mask[i] = True
            M -= 1
        K -=  1
        if M == 0:
            break
    array = array[mask,...]
    SBM1 = 0
    SBM2 = 0
    SBM3 = 0
    for row in array:
        SBM1 += row[5]
        SBM2 += row[6]
        SBM3 += row[7]
    SBM1 /= 5000
    SBM2 /= 5000
    SBM3 /= 5000
    print(array[0])
    print(SBM1)
    print(SBM2)
    print(SBM3)
    end = time.time()
    print(end-start)

def task5_numpy():
    start = time.time()
    array = get_array()
    mask = numpy.zeros(len(array),dtype=bool)
    for i,row in enumerate(array):
        if (int(row[0][11]+row[0][12]) >= 18):
            mask[i] = True
    array = array[mask,...]
    array = array[numpy.where(array["GAP"]>6,array["SM2"]>array["SM3"],array["SM2"]>array["SM1"])]
    mask = numpy.zeros(len(array),dtype=bool)
    i = 0
    while i <= len(array)/2:
        if i % 3 == 0: 
            mask[i] = True
        i+= 1
    while i < len(array):
        if i % 4 == 0:
            mask[i] = True
        i+= 1
    array = array[mask,...]
    print(array[0])
    end = time.time()
    print(end-start)

task5_numpy()
