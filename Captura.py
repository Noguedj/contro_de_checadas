import RPi.GPIO as GPIO #importar librerias de GPIO
prueba = open("/home/pi/Downloads/2pase.txt","w")
prueba.write("\r\n")
prueba.close()
while 1 == 1:
    encontrado = "reset"
    import time
    hora = time.strftime("%H%M")
    fecha = time.strftime("%y%m%d")
    print("Introduce el numero de empleado\n")
    Num = raw_input()
    with open("/home/pi/Downloads/2pase.txt","r") as f:
        lineas = [linea.split() for linea in f]
    for linea in lineas:
        if linea == [Num]:
            encontrado = "si"
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(19, GPIO.OUT)
            GPIO.output(19,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(19,GPIO.LOW)
            break
        else:
             encontrado = "no"
    if encontrado == "no":
        with open("/home/pi/Downloads/usr","r") as f:
            lineas = [linea.split() for linea in f]
        for linea in lineas:
            if linea == [Num]:
               encontrado = "si"
               prueba = open("/home/pi/Downloads/Estacion_12.txt","a")
               prueba.write(Num)
               prueba.write("21")
               prueba.write(fecha)
               prueba.write(hora)
               prueba.write("\r\n")
               prueba.close()
               prueba = open("/home/pi/Downloads/2pase.txt","a")
               prueba.write(Num)
               prueba.write("\r\n")
               prueba.close()
               GPIO.setmode(GPIO.BCM)
               GPIO.setup(19, GPIO.OUT)
               GPIO.output(19,GPIO.HIGH)
               time.sleep(1)
               GPIO.output(19,GPIO.LOW)
               break
            else:
               encontrado = "no"
    if encontrado == "no":
   	GPIO.setmode(GPIO.BCM)
   	GPIO.setup(26, GPIO.OUT)
   	GPIO.output(26,GPIO.HIGH)
  	time.sleep(1)
    	GPIO.output(26,GPIO.LOW)

