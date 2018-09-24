import cv2
import sys
#import open cv
import numpy as np
#import numpy for scientific calculations
from matplotlib import pyplot as plt
#display the image
from PIL import ImageTk
from PIL import Image as im
from scipy import ndimage
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pylab as pl
from os import listdir
import webcolors as webcolors
import neurolab as nl
import sys

np.set_printoptions(suppress=True)
global decision
global decisionRecorte
global x
global y
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

net = nl.load('test.net')
#a8

inFile = sys.argv[1]
with open(inFile,'r') as i:
    lines = i.readlines()

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


def chooser():
	val = askopenfilename()
	return val;


def recorteVal(val):
	return val

def ventanaRecorte(banana):
	global root
	root = Tk()
	root.title("Labeler")
	root.geometry("1050x600")


	cv2.imwrite('ventana/opcion1_resize.jpg',banana)

	img = ImageTk.PhotoImage(im.open('ventana/opcion1_resize.jpg'))

	panel = Label(root, image = img)
	#panel.pack(side = "bottom", fill = "both", expand = "yes")
	app = Frame(root)
	app.grid()
	label = Label(app, text="Elige la opcion que mejor detecto el banano")
	panel.grid()
	root.bind('<Button-1>', motion)
	root.mainloop()

def ventana(valor):
	global root
	root = Tk()
	root.title("DETECCION DE BANANOS")
	root.geometry("800x600")


	if valor ==1 :
		imagen=cv2.imread('ventana/opcion1.jpg')
		cv2.imwrite('pruebaVentana.jpg',imagen)
	else:
		imagen=cv2.imread('ventana/opcion2.jpg')

	imagen = cv2.resize(imagen,(400, 400))


	cv2.imwrite('ventana/opcion1_resize.jpg',imagen)


	img = ImageTk.PhotoImage(im.open('ventana/opcion1_resize.jpg'))



	panel = Label(root, image = img)

	#panel.pack(side = "bottom", fill = "both", expand = "yes")
	app = Frame(root)
	app.grid()
	label = Label(app, text="El Banano fue correctamente detectado?")

	boton1 = Button(app,text="SI")
	boton1.bind('<Button-1>',funcion)
	boton2 = Button(app,text="NO")
	boton2.bind('<Button-1>',funcion2)



	label.config(font=30)
	label.grid(row=0, column=200)
	boton1.grid(row=1, column=150)
	boton2.grid(row=1, column=200)

	panel.config(height=500)
	panel.grid(row=40)
	print("aqui muestra ventana")


	root.mainloop()

def motion(event):
    x, y = event.x, event.y;	print(x,y);cortarUser(x,y);


def funcion(event):
	global decisionRecorte
	decisionRecorte=1

def funcion2(event):
	global decisionRecorte
	decisionRecorte=0
# def funcion2(event):
# 	global decisionRecorte
#     decisionRecbananaorte=2

def find_biggest_contour(image):
	image=image.copy()
	_ , contours , hierarchy=cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	contour_sizes=[(cv2.contourArea(contour),contour) for contour in contours]
	biggest_contour=max(contour_sizes,key=lambda x:x[0])[1]
	mask=np.zeros(image.shape,np.uint8)
	cv2.drawContours(mask,[biggest_contour],-1,255,-1)

	return biggest_contour,mask

def overlay_mask(mask,image):
	rgb_mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
	img=cv2.addWeighted(rgb_mask,0.5,image,0.5,0)
	return img

def bananoLimpio(imagen,val):
	img = cv2.imread('img3.jpg')
	altura = imagen.shape[1]
	ancho = imagen.shape[0]
	resized_imagen = cv2.resize(img, (altura, ancho))
	cv2.ellipse(resized_imagen,ellipse,red,2,1)
	if val==1:

		cv2.imwrite('ventana/opcion1.jpg',resized_imagen)
	else:
		cv2.imwrite('ventana/opcion2.jpg',resized_imagen)
	print(ancho)
	print(altura)


def circle_contour(image,contour):

	image_with_ellipse=image.copy()
	global ellipse
	ellipse=cv2.fitEllipse(contour)

	global centros
	global distancias
	global angulo
	centros = ellipse[0]
	distancias = ellipse[1]
	angulo = ellipse[2]
	print("centroX {}".format(ellipse[0][0]))
	print("centroY {}".format(ellipse[0][1]))
	cv2.ellipse(image_with_ellipse,ellipse,red,2,1)
	return image_with_ellipse

def cortarUser(x,y):
    crop_img = banana[int(y):int(y)+70,int(x):int(x)+70];	cv2.imwrite('cortar.jpg',crop_img);

def show(image):
	plt.figure(figsize=(10,10))
	plt.imshow(image,interpolation='nearest')

	#min_color=np.array([130,0,0]) max_color=np.array([170,255,255]) mascaras para color negro
	#min_color=np.array([15,100,80]) max_color=np.array([105,255,255]) mascaras para demas colores
def draw_banana(image,min_color,max_color):
	#PRE PROCESSING OF IMAGE
	image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	maxsize=max(image.shape)
	scale=700/maxsize
	image=cv2.resize(image,None,fx=scale,fy=scale)
	image_blur=cv2.GaussianBlur(image,(7,7),0)
	image_blur_hsv=cv2.cvtColor(image_blur,cv2.COLOR_RGB2HSV)

	mask1=cv2.inRange(image_blur_hsv,min_color,max_color)
	min_color2=np.array([170,100,80])
	max_color2=np.array([180,255,255])
	mask2=cv2.inRange(image_blur_hsv,min_color2,max_color2)
	mask=mask1+mask2
	kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
	#print kernel solo muestra un puunto
	#cambiar los parametros (15,15) solo cambia el grosor de la linea de la elipse
	# cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)).getRadius no esta disponible en cv2
	mask_closed=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
	mask_cleaned=cv2.morphologyEx(mask_closed,cv2.MORPH_OPEN,kernel)
	big_contour,mask_fruit=find_biggest_contour(mask_cleaned)
	overlay=overlay_mask(mask_cleaned,image)
	#print overlay solo mustra el banano sin la elipse
	circled=circle_contour(overlay,big_contour)
	#circled es el banano con un overlay aplicado
	show(circled)
	bgr=cv2.cvtColor(circled,cv2.COLOR_RGB2BGR)

	return bgr

def cortar(val):
	if val == 1:
		img = cv2.imread("ventana/opcion1.jpg")
	else:
		img = cv2.imread("ventana/opcion2.jpg")

	print(centros)
	crop_img = img[ (int(centros[1])-(int(distancias[1]*0.25))):(int(centros[1])+(int(distancias[1]*0.25))), (int(centros[0])-(int(distancias[0]*0.25))):(int(centros[0])+(int(distancias[0]*0.25)))                     ]
	 # Crop from x, y, w, h -> 100, 200, 300, 400
	# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

	cv2.imwrite('cortar.jpg',crop_img)
	ban=cv2.imread('cortar.jpg')
	resized_image = cv2.resize(ban,(70, 70))
	cv2.imwrite('cortar.jpg',resized_image)

def mapeo(x, in_min, in_max, out_min = 0, out_max = 10.):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#Funciones Para Red

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



def cargarRed(val):

	im2 = im.open('cortar.jpg')
	im3 = im2.convert("RGB")

	pixels = list(im3.getdata())
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


	entrada = [[contRed, contOrange, contDarkGreen, contLightGreen, contLightYellow, contDarkYellow, contBrown, contBlack]]
	global out
	out = net.sim(entrada)
	print (out)

#fin  funciones Red




global banana
banana = cv2.imread(str(sys.argv[1]))


try:
#ejecucion de banano con mascaras claras

	result_banana=draw_banana(banana,np.array([15,100,80]),np.array([105,255,255]))

#imagen girada por el angulo de la primera elipse encontrada
	rotacion = ndimage.rotate(banana, angulo)
	cv2.imwrite('img3.jpg',rotacion)#se crea la segunda ellipse rotada 0 en su angulo
	bananaRotada = cv2.imread('img3.jpg')
	result_banana = draw_banana(bananaRotada,np.array([15,100,80]),np.array([105,255,255]))
	bananoLimpio(result_banana,1)

	ventana(1)

	if decisionRecorte== 1:
		cortar(1)
#ejecucion de banano mascaras oscuras
	else:

		result_banana=draw_banana(banana,np.array([130,0,0]),np.array([170,255,255]))
		#imagen girada por el angulo de la primera elipse encontrada
		rotacion = ndimage.rotate(banana, angulo)
		cv2.imwrite('img3.jpg',rotacion)#se crea la segunda ellipse rotada 0 en su angulo
		bananaRotada = cv2.imread('img3.jpg')
		result_banana=draw_banana(bananaRotada,np.array([130,0,0]),np.array([170,255,255]))
		bananoLimpio(result_banana,2)
		ventana(2)
		if decisionRecorte == 1:
			cortar(2)
except Exception:
	try:

		result_banana=draw_banana(banana,np.array([130,0,0]),np.array([170,255,255]))
		#imagen girada por el angulo de la primera elipse encontrada
		rotacion = ndimage.rotate(banana, angulo)
		cv2.imwrite('img3.jpg',rotacion)#se crea la segunda ellipse rotada 0 en su angulo
		bananaRotada = cv2.imread('img3.jpg')
		result_banana=draw_banana(bananaRotada,np.array([130,0,0]),np.array([170,255,255]))
		bananoLimpio(result_banana,2)
		ventana(2)
		if decisionRecorte == 1:
			cortar(2)


			result_banana = draw_banana(banana,np.array([130,0,0]),np.array([170,255,255]))
			#imagen girada por el angulo de la primera elipse encontrada
			rotacion = ndimage.rotate(banana, angulo)
			cv2.imwrite('img3.jpg',rotacion)#se crea la segunda ellipse rotada 0 en su angulo
			bananaRotada = cv2.imread('img3.jpg')
			result_banana=draw_banana(bananaRotada,np.array([130,0,0]),np.array([170,255,255]))
			bananoLimpio(result_banana,2)
			ventana(2)
			if decisionRecorte == 1:
				cortar(1)
	except Exception:
		print("No se puede reconocer el banano")
		global decision
		decision = 0
if decisionRecorte == 0:
	ventanaRecorte(banana)
cargarRed(banana)

arreglo = out[0]
pos = 0
mayor = arreglo[0]

for i in range(len(arreglo)):
	if arreglo[i] > mayor:
		mayor = arreglo[i]
		pos = i


if pos == 0:
	if (arreglo[0] - arreglo[1]) < 0.1:
		messagebox.showinfo("¡Ups, verde todavia!", "10'%' \nPrueba en unos cinco dias...\n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 5 dias \nTiempo aproximado para su caducidad: 22 dias")
	else:
		messagebox.showinfo("¡Ups, demasiado verde!", "0'%' \nEl estado de maduración del banano que has elegido es muy temprano. Para su consumo, puedes probar de nuevo a partir de diez dias \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 15 dias \nTiempo aproximado para su caducidad: 27 dias")
elif pos == 1:
	if (arreglo[1] - arreglo[0]) < 0.1:
		messagebox.showinfo("Espera otro poquito...", "15'%' \nTu banano recien empieza a madurar. Puede estar amargo si lo comes asi. Espera siete dias y vuelve por aca \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 6-7 dias \nTiempo aproximado para su caducidad: 20 dias")
	elif (arreglo[1] - arreglo[2]) < 0.1:
		messagebox.showinfo("Espera otro poquito...", "30'%' \n¡Ya casi! Puedes arriesgarte o esperar otro poquito \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 2 dias \nTiempo aproximado para su caducidad:  16-17dias")
	else:
		messagebox.showinfo("Espera otro poquito...", "20'%' \nTodavia le falta otro poquito :)")
elif pos == 2:
	if (arreglo[2] - arreglo[1]) < 0.1:
		messagebox.showinfo("¡Llegó el momento!", "40'%' \n¡Por fin ha alcanzado su madurez! Tienes un aproximado de nueve días. \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 11 dias")
	elif (arreglo[2] - arreglo[3]) < 0.1:
		messagebox.showinfo("¡Llegó el momento!","60'%'E\nstá listo, pero los días están pasando. Te quedan cerca de cinco días... \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 7 dias" )
	else:
		messagebox.showinfo("¡Llegó el momento!","50'%' \nEn su punto. Tienes aproximadamente una semana. \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 9 dias")
elif pos == 3:
	if (arreglo[3] - arreglo[2]) < 0.1:
		messagebox.showinfo("¡Todavía estás a tiempo!","65'%' \nEl tiempo pasa. Quedan cerca de cuatro dias antes de que no puedas comerte el banano \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 5-6 dias")
	elif (arreglo[3] - arreglo[4]) < 0.1:
		messagebox.showinfo("¡Queda poco tiempo!","75'%' \n¡Apresúrate! Todavía Estás a tiempo ;) \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 4 dias")
	else:
		messagebox.showinfo("¡Ahora o nunca!","70'%' \nQueda poco tiempo. Caducará de cuatro a dos días. \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 2-4 dias")
elif pos == 4:
	if arreglo[4] - arreglo[3] < 0.1:
		messagebox.showinfo("¡Ups! Creo que ya no es buena idea","80'%' \nEs muy posible que tu banano no esté en condiciones para ser digerido. Verifica que no tenga heridas en su cáscara, si te animas... \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 1-2 dias" )
	else:
		messagebox.showinfo("Ni lo intentes...","100'%' \nEl banano caducó. No lo consumas, puede ser peligroso \n\nTiempo aproximado para porcentaje de maduracion apto para el consumo: 0 dias \nTiempo aproximado para su caducidad: 0 dias")
