import webcolors

primeraetapa = (
'darkolivegreen',
'olivedrab',
'olive',
'yellowgreen',
'limegreen',
'lime',
'lawngreen',
'chartreuse',
'greenyellow',
'springgreen',
'mediumspringgreen',
'lightgreen',
'palegreen',
'darkseagreen',
'mediumaquamarine',
'mediumseagreen',
'seagreen',
'forestgreen',
'green',
'darkgreen'
)


etapamedia = (
'yellow',
'lightyellow',
'lemonchiffon',
'lightgoldenrodyellow',
'papayawhip',
'moccasin',
'peachpuff',
'palegoldenrod',
'khaki',
'darkkhaki',
'goldenrod'
)


etapafinal = (
'darkgoldenrod',
'peru',
'chocolate',
'saddlebrown',
'sienna',
'brown',
'maroon',
'silver',
'darkgray',
'gray',
'dimgray',
'lightslategray',
'slategray',
'darkslategray',
'black'
)


negro = False
verde = False
amarillo = False
contN = 0
contV = 0
contA = 0


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

requested_colour = (190, 188, 199)
actual_name, closest_name = get_colour_name(requested_colour)

print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)


for iterador in range(len(etapafinal)):
    if closest_name is etapafinal[iterador]:
        negro = True
        contN += 1

for iterador in range(len(etapamedia)):
    if closest_name is etapamedia[iterador]:
        amarillo = True
        contA += 1

for iterador in range(len(primeraetapa)):
    if closest_name is primeraetapa[iterador]:
        verde = True
        contV += 1


negro, verde, amarillo  = False, False, False
# print (contV)
# print (contA)
# print (contN)
