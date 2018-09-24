

El fin de este proyecto es el procesamiento de imagenes por medio de una aplicación,
especificamente de fotografías de bananos. Al pasar la fotografía por la aplicación,
mostrará la misma con una elipse, y preguntará al usuario si ha sido correctamente.
Es posible que la detección vuelva a fallar, o no diagnostique la parte del banano
que el usuario desea analizar. Por lo tanto, se tendrá la oportunidad de darle click
a la región que el usuario desee pasar por la IA para reconocer su estado de madurez.


Ejecución:

1) Abrir terminal
2) buscar carpeta raiz de la aplicacion
3)entrar en carpeta reconocimientoColor
	Nota en esta carpeta se colocaran las imagenes que se quieren analizar
4) ejecutar el siguiente comando:

	python dibujarBanano.py ejemplo.jpg

ejemplo.py es el nombre de la imagen que se desea analizar.

5) cuando el script se ejecuta se desplegaran dos opciones de deteccion del banano,en estas el usuario debe ingresar
 si el banano fue detectado.

 opcion 1
	el banano se detecto correctamente presionar si y cerrar la ventana que se desplego.
	
 opcion 2
	la deteccion no fue correcta presionar no y  cerrar ventana

 opcion 3
	si la deteccion fallo dos veces ahora se presenta una tercera opcion esta es para que el usuario eliga que area del 
	banano desea analizar.Asi que solo debe dar click en el area y cerrar la ventana

6) cuando la deteccion ya sea la correcta se desplegaran los estados del banano y su tiempo para consumo o maduracion.
	

requisitos:

- para el correcto funcionamiento de la aplicacion se debe utilizar python 3
- libreria neurolab
- libreria tkinter
- libreria numpy
- libreria PIL
- libreria cv2
- libreria pylab
- libreria sys 
- libreria webcolors
- libreria matplotlib
- libreria scipy



