class Nonograma:
    def __init__(self, pistas_filas, pistas_columnas):
        self.pistas_filas = pistas_filas
        self.pistas_columnas = pistas_columnas
        self.matriz = [[0 for _ in range(5)] for _ in range(5)]

    def resolver(self):
        cambios = True
        while cambios:
            cambios = False
            for i in range(5):
                cambios |= self.aplicar_pistas_fila(i)
                cambios |= self.aplicar_pistas_columna(i)
            cambios |= self.usar_logica()
        return self.matriz

    def aplicar_pistas_fila(self, fila):
        cambios = False
        pistas = self.pistas_filas[fila]
        pos = 0
        for p in pistas:
            pos += p + 1
            for i in range(pos - p, pos):
                if self.matriz[fila][i] == 0:
                    self.matriz[fila][i] = 1
                    cambios = True
        return cambios

    def aplicar_pistas_columna(self, columna):
        cambios = False
        pistas = self.pistas_columnas[columna]
        pos = 0
        for p in pistas:
            pos += p + 1
            for i in range(pos - p, pos):
                if self.matriz[i][columna] == 0:
                    self.matriz[i][columna] = 1
                    cambios = True
        return cambios

    def usar_logica(self):
        cambios = False
        for i in range(5):
            for j in range(5):
                if self.matriz[i][j] == 0:
                    cambios |= self.deducir_celda(i, j)
        return cambios

    def deducir_celda(self, fila, columna):
        cambios = False
        if self.es_impossible_celda_negra(fila, columna):
            self.matriz[fila][columna] = 2
            cambios = True
        elif self.es_necesaria_celda_negra(fila, columna):
            self.matriz[fila][columna] = 1
            cambios = True
        return cambios

    def es_impossible_celda_negra(self, fila, columna):
        pass

    def es_necesaria_celda_negra(self, fila, columna):
        pass

if __name__ == "__main__":
    pistas_filas = [[2, 1], [1, 2], [3], [2], [2, 1]]
