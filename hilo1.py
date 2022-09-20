import time
import threading 

count=1

#FUNCIONO A EJECUTAR
def account(n, name):
	global count
	loop = 1
	while loop<5:
		print(name, count)
		count+=1
		loop+=1

#CREAMOS PROCESOS A EJECUTAR EN PARALELO
# El proceso va a tener 4 hilos, ya que el procesos simpre se inicia con uno
t1 = threading.Thread(target = account, args=(2,'thread1'))
t2 = threading.Thread(target=account, args=(1, 'thread2'))
t3 = threading.Thread(target=account, args=(1, 'thread3'))

#INICIAMOS PROCESO
t1.start()
time.sleep(3)
t2.start()
time.sleep(3)
t3.start()


# OUT OF CODING
# La memoria count esta siendo compartida por 3 hilos en total son 4 hilos.
# Como resultados hilos se tapan entre si. 
# Con los sleep podemos hacerlo en serie y no solapar la memoria