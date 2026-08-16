class TimeMap:
    def __init__(self):
        self.timeList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # si la key no existe, creamos el array principal
        if self.timeList.get(key,-1) == -1:
            self.timeList[key] = []

        # agregamos el array al array
        tupleL = (timestamp,value)
        self.timeList[key].append(tupleL)

    def get(self, key: str, timestamp: int) -> str:
        # primero comprobar que existe la llave
        if self.timeList.get(key,-1) == -1:
            return ""
        
        # guardamos los valores para ahorrar llamadas
        valores = self.timeList[key]

        # buscar el valor mediante binary search
        left = 0
        rigth = len(valores) -1

        while(left <= rigth):
            mid = left + (rigth - left)//2

            if valores[mid][0] == timestamp:
                return valores[mid][1]
            
            if valores[mid][0] > timestamp:
                rigth = mid -1 
            else:
                left = mid + 1

        # si no lo encuentra, rigth ya debe estar ahi
        if rigth >= 0:
            return valores[rigth][1]
        return ""