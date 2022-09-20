from ast import If
from multiprocessing import Process, Pipe

def f(conn1, frase):
    conn1.send(frase)

def f1(conn2):
    print(conn2.recv())

def main():
    frase = input("Frase: ")
    conn1, conn2 = Pipe()
    p = Process(target=f, args= (conn1, frase))
    p.start()
    p.join()
    p1 = Process(target=f1, args=(conn2,))
    p1.start()
    p1.join()

if __name__ == '__main__':
    main()
