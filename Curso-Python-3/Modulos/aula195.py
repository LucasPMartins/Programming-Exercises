from time import sleep
from threading import Thread
from threading import Lock

# print('Hello')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('World!')

# class MeuThread(Thread):
#     def __init__(self,texto,tempo):
#         self.texto = texto
#         self.tempo = tempo
#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MeuThread('Thread 1',5)
# t1.start()

# t2 = MeuThread('Thread 2',3)
# t2.start()

# t3 = MeuThread('Thread 3',2)
# t3.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# def vai_demorar(texto,tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar,args=("Olá mundo 1!",5))
# t1.start()
# t2 = Thread(target=vai_demorar,args=("Olá mundo 2!",1))
# t2.start()
# t3 = Thread(target=vai_demorar,args=("Olá mundo 3!",2))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(.5)

# def vai_demorar(texto,tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar,args=("Olá mundo 1!",10))
# t1.start()
# t1.join() # Espera acabar

# # while t1.is_alive():
# #     print('Esperando a thread.')
# #     sleep(2)

# print("Thread acabou!")

class Ingressos:
    def __init__(self,estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self,quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("Não temos ingressos suficientes.")
            self.lock.release()
            return
        sleep(1)
        self.estoque -= quantidade
        print(f"Você comprou {quantidade} ingressos. "\
              f'Ainda temos {self.estoque} em estoque.')
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1,20):
        t = Thread(target=ingressos.comprar,args=(i,))
        t.start()

    print(ingressos.estoque)