import os

CONSULTAR = '_Consultar'
EXTRAS = '_Extras'
RESERVAR = '_Reservar'
VISUALUZAR = '_Visualizar'
CANCELAR = '_Cancelar'

METHODS = [CONSULTAR, EXTRAS, RESERVAR, VISUALUZAR, CANCELAR]

USE_ABSTRACT = 'use AbstractLocadoraWs;'
CLASS = 'class'
ABSTRACT_CLASS = 'abstract ' + CLASS
EXTENDS = ' extends '

# driverExistents = input('O Driver já existe ? ')
# driverExistents = 'Sim'

# if driverExistents:
# driverName = input('Qual o nome do Driver ? ')
driverName = 'TurevracDriver'

# rentalName = input('Qual o nome da locadora ? ')
rentalName = 'NissaImplementacao'

dirDriverWs = 'common/DriverWs/' + driverName
dirRentalWs = 'common/LocadoraWs/' + rentalName

os.mkdir(dirDriverWs)
os.mkdir(dirRentalWs)

fileName = rentalName + '.php'


def createMethodsDriverWs():
    for method in METHODS:
        methodsDriverWs = open(dirDriverWs + '/' + driverName + method + '.php', "x")
        print(methodsDriverWs.name)
        methodsDriverWs.close()

        f = open(methodsDriverWs.name, "w")
        f.write("<?php")
        f.write("\n\n")
        f.write(USE_ABSTRACT)
        f.write("\n\n\n")
        f.write(ABSTRACT_CLASS + ' ' + driverName + method)
        f.write("\n")
        f.write("{")
        f.write("\n")
        f.write("}")
        print(f.name)
        f.close()

    driverWs = open('common/DriverWs/' + driverName + '.php', "x")
    driverWs.close()


def createMethodsLocadoraWs():
    for method in METHODS:
        methodsLocadoraWs = open(dirRentalWs + '/' + rentalName + method + '.php', "x")
        print(methodsLocadoraWs.name)
        methodsLocadoraWs.close()

        f = open(methodsLocadoraWs.name, "w")
        f.write("<?php")
        f.write("\n\n")
        f.write(USE_ABSTRACT)
        f.write("\n\n\n")
        f.write(CLASS + ' ' + rentalName + method + EXTENDS)
        f.write("\n")
        f.write("{")
        f.write("\n")
        f.write("}")
        print(f.name)
        f.close()

    locadoraWs = open('common/LocadoraWs/' + rentalName + '.php', "x")
    locadoraWs.close()


createMethodsDriverWs()

createMethodsLocadoraWs()
