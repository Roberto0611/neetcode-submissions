class TimeMap:
    def __init__(self):
        self.timeList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # si la key no existe, creamos el array principal
        if self.timeList.get(key,-1) == -1:
            self.timeList[key] = []

        # agregamos el array al array
        array = [timestamp,value]
        self.timeList[key].append(array)

    def get(self, key: str, timestamp: int) -> str:
        # primero comprobar que existe la llave
        if self.timeList.get(key,-1) == -1:
            return ""
        
        # buscar el valor mediante binary search
        left = 0
        rigth = len(self.timeList[key]) -1

        #self.timeList[key][variable][0])

        while(left <= rigth):
            mid = left + (rigth - left)//2

            if self.timeList[key][mid][0] == timestamp:
                return self.timeList[key][mid][1]
            
            if self.timeList[key][mid][0] > timestamp:
                rigth = mid -1 
            else:
                left = mid + 1
        # si no lo encuentra
        if self.timeList[key][mid][0] > timestamp:
            #buscar hacia atras
            i = mid
            for i in range(mid,-1,-1):
                if self.timeList[key][i][0] < timestamp:
                    return self.timeList[key][i][1]
            return ""
        return self.timeList[key][mid][1]