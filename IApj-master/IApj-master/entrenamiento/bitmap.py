from PIL import Image
import numpy as np
import webcolors as webcolors
from os import listdir

redcolors = (
'lightsalmon',
'salmon',
'darksalmon',
'lightcoral',
'indianred',
'crimson',
'firebrick',
'darkred',
'red'
)

orangecolors = (
'orangered',
'tomato',
'coral',
'darkorange',
'orange'
)


verdeOscuro = (
'darkolivegreen',
'olive',
'olivedrab',
'yellowgreen',
'limegreen',
'darkseagreen',
'mediumaquamarine',
'mediumseagreen',
'seagreen',
'forestgreen',
'green',
'darkgreen'
)


verdeClaro = (
'lime',
'lawngreen',
'chartreuse',
'greenyellow',
'springgreen',
'mediumspringgreen',
'lightgreen',
'palegreen'
)


amarillosC = (
'lightyellow',
'lemonchiffon',
'lightgoldenrodyellow',
'papayawhip',
'moccasin',
'peachpuff',
)

amarillosO = (
'yellow',
'lightyellow',
'palegoldenrod',
'khaki',
'darkkhaki',
'goldenrod',
)


brown = (
'darkgoldenrod',
'peru',
'chocolate',
'saddlebrown',
'sienna',
'brown',
'maroon',
)

black = (
'silver',
'darkgray',
'darkgrey',
'grey',
'gray',
'dimgray',
'dimgrey',
'lightslategray',
'lightslategrey',
'slategray',
'slategrey',
'darkslategray',
'darkslategrey',
'black'
)


def displayImage(image):
    displayList=np.array(image).T
    im1 = Image.fromarray(displayList)
    im1.show()

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name



arrayFotos = []

for cosa in listdir("."):
    if cosa[-4:] == ".jpg":
        arrayFotos.append(cosa)

for iterador in range(len(arrayFotos)):
    #print (arrayFotos[iterador])

    im2 = Image.open(arrayFotos[iterador])
    im = im2.convert("RGB")

    pixels = list(im.getdata())
    contRed = 0
    contOrange = 0
    contDarkGreen = 0
    contLightGreen = 0
    contLightYellow = 0
    contDarkYellow = 0
    contBrown = 0
    contBlack = 0

    for dato in range(4900):
        actual_name, closest_name = get_colour_name(pixels[dato])
        # buscarDato(closest_name)
        #print(actual_name)
        for iterador in range(len(redcolors)):
            if closest_name is redcolors[iterador]:
                contRed += 1

        for iterador in range(len(orangecolors)):
            if closest_name is orangecolors[iterador]:
                contOrange += 1

        for iterador in range(len(verdeOscuro)):
            if closest_name is verdeOscuro[iterador]:
                contDarkGreen += 1

        for iterador in range(len(verdeClaro)):
            if closest_name is verdeClaro[iterador]:
                contLightGreen += 1

        for iterador in range(len(amarillosC)):
            if closest_name is amarillosC[iterador]:
                contLightYellow += 1

        for iterador in range(len(amarillosO)):
            if closest_name is amarillosO[iterador]:
                contDarkYellow += 1

        for iterador in range(len(brown)):
            if closest_name is brown[iterador]:
                contBrown += 1

        for iterador in range(len(black)):
            if closest_name is black[iterador]:
                contBlack += 1


    contRed = (contRed * 100) / 4900
    contOrange = (contOrange * 100) / 4900
    contDarkGreen = (contDarkGreen * 100) / 4900
    contLightGreen = (contLightGreen * 100) / 4900
    contLightYellow = (contLightYellow * 100) / 4900
    contDarkYellow = (contDarkYellow * 100) / 4900
    contBrown = (contBrown * 100) / 4900
    contBlack = (contBlack * 100) / 4900

    contRed =  round(contRed, 2)
    contOrange = round(contOrange, 2)
    contDarkGreen = round(contDarkGreen, 2)
    contLightGreen = round(contLightGreen, 2)
    contLightYellow = round(contLightYellow, 2)
    contDarkYellow = round(contDarkYellow, 2)
    contBrown = round(contBrown, 2)
    contBlack = round(contBlack, 2)


    print ("Rojo:               ","%.2f" %contRed + "%")
    print ("Naranja:            ","%.2f" %contOrange + "%")
    print ("Verde Oscuro:       ","%.2f" %contDarkGreen + "%")
    print ("Verde Claro:        ","%.2f" %contLightGreen + "%")
    print ("Amarillo Claro:     ","%.2f" %contLightYellow + "%")
    print ("Amarillo Oscuro:    ","%.2f" %contDarkYellow + "%")
    print ("Cafe:               ","%.2f" %contBrown + "%")
    print ("Negro:              ","%.2f" %contBlack + "%")

    arregloMaduracion = []
    im2.show()
    ##omega = input('En qué estado de maduración está el banano VERDE[1]  MAS AMARILLO QUE VERDE[2]  AMARILLO[3]    AMARILLO MOTEADO[4]   AMARILLO MANCHADO[5]    NEGRO[6] ?  ')
    omega = input('En qué estado de maduración está el banano [1 - 5] ?  ')
    if omega == '1':
        arregloMaduracion = [1,0,0,0,0]
    elif omega == '2':
        arregloMaduracion = [0,1,0,0,0]
    elif omega == '3':
        arregloMaduracion = [0,0,1,0,0]
    elif omega == '4':
        arregloMaduracion = [0,0,0,1,0]
    elif omega == '5':
        arregloMaduracion = [0,0,0,0,1]

    cadena =  str(contRed) + " " + str(contOrange) + " " + str(contDarkGreen) + " " + str(contLightGreen) + " " + str(contLightYellow) + " "  + str(contDarkYellow) + " " + str(contBrown) + " " + str(contBlack) + " "  + str(arregloMaduracion[0]) + " " + str(arregloMaduracion[1]) +  " " + str(arregloMaduracion[2]) +  " " + str(arregloMaduracion[3]) +  " " + str(arregloMaduracion[4])
    f = open("entrada.csv",'a')
    f.seek(0,2)
    f.write(str(cadena) + '\n')
    f.close()
