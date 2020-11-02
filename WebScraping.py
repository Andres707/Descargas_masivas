import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')


class web_scr:
    def __init__(self):
        self.uniondatos = list()
        self.statusf = bool
        # llamada = self.llamada(url)
        # conj = self.conjuntos(llamada)
        # print('estado: {}'.format(llamada))
        # print(self.busqueda(conj, 'h1'))
        # print(self.busqueda(conj, 'a'))
        # print(url)
        # url = url + '-1'
        # print(url)
        # predatos = dict()
        # for i in range(3):
        #     predatos[i]= {
        #         'nombre': 'hola ' + str(1),
        #         'estado': 200,
        #         'link': ['1', '2', '3']
        #     }
        #
        # print(predatos)
        # print(self.getdatos())

    def ran(self, url, max, min):
        hiloweb = threading.Thread(name='hiloWeb', target=self.run, args=(url, max, min))
        hiloweb.isDaemon()
        hiloweb.start()

    def run(self, url, max, min):
        self.statusf = False
        # dicc = dict()
        for i in range(min, max + 1, 1):
            url1 = url + '-{}'.format(i)
            llamada = self.llamada(url1)
            conjuntos = self.conjuntos(llamada)
            a = list()
            contador = 1
            for j in self.busqueda(conjuntos, 'a'):
                a.append([contador, j['href']])
                contador += 1
            h1 = list()
            for j in self.busqueda(conjuntos, 'h1'):
                h1.append(j.text)
            for y in range(len(a)):
                estado = self.estado(self.llamada(a[y][1]))
                a[y].append(estado)
            self.uniondatos.append([h1[0], a])
            # print(uniondatos)
        self.statusf = True

    def getdatos(self):
        if self.statusf == True:
            return self.uniondatos
        else:
            return 'Cargando...'

    def creacion_csv(self, dicc):
        df = pd.DataFrame(dicc)
        df.to_csv('datos/covidHidalgoCompleto.csv', header=True, index=False)

    def llamada(self, url):
        headers = {'user-agent': 'my-app/0.0.1'}
        return requests.get(url, headers)

    def conjuntos(self, page):
        return BeautifulSoup(page.content, 'html.parser')

    def busqueda(self, conjunt, dato):
        if dato == 'h1':
            return conjunt.find_all(dato, class_='Title')
        else:
            return conjunt.find_all(dato, class_='Button Sm fa-download')

    def estado(self, codigo):
        return codigo.status_code

# if __name__ == '__main__':
#     t = web_scr()
#     web_scr.ran(self=t,url='https://www3.animeflv.net/ver/sword-art-online-alicization-war-of-underworld', max=2, min=1)