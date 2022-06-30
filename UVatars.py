

from bottle import get, post, run, request, template, route
import sys
import json
import random


#Función que sirve para crear un uvatar aleatorio (formato json) cogiendo partes aleatoriamente del UVatars.json
def UVatarAleatorio():

    UVatarRandom = {}
    with open('UVatars.json') as file:
        data = json.load(file)

    numBoca = random.randint(0,3)
    numNariz = random.randint(0,3)
    numOjos = random.randint(0,3)
    numPelo = random.randint(0,3)
    numOrejaI = random.randint(0,3)
    numOrejaD = random.randint(0,3)

    UVatarRandom["bocas"] = data["bocas"][numBoca]
    UVatarRandom["narices"] = data["narices"][numNariz]
    UVatarRandom["ojos"] = data["ojos"][numOjos]
    UVatarRandom["pelos"] = data["pelos"][numPelo]
    UVatarRandom["orejasI"] = data["orejasI"][numOrejaI]
    UVatarRandom["orejasD"] = data["orejasD"][numOrejaD]

    return UVatarRandom

#Funciones que meten los json de las caras en una variable
def caraBicho():
    with open('caraBicho.json') as file:
        data = json.load(file)
    return data

def caraMessi():
    with open('caraMessi.json') as file:
        data = json.load(file)
    return data

def caraPedri():
    with open('caraPedri.json') as file:
        data = json.load(file)
    return data

def caraAraujo():
    with open('caraAraujo.json') as file:
        data = json.load(file)
    return data
    


#Métodos @get y @post para subir los distintos json creados a su respectivo http

@get('/Aleatorio')
def hola():
    al = UVatarAleatorio()
    return al

@post('/Aleatorio')
def uvatarAleatorio():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/caraBicho')
def hola():
    return caraBicho()

@post('/caraBicho')
def mostrarCaraBicho():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body
@get('/caraMessi')
def hola():
    return caraMessi()

@post('/caraMessi')
def mostrarCaraMessi():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/caraPedri')
def hola():
    return caraPedri()

@post('/caraPedri')
def mostrarCaraPedri():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/caraAraujo')
def hola():
    return caraAraujo()

@post('/caraAraujo')
def mostrarCaraAraujo():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body


run(host='localhost', port=8080, debug=True)


