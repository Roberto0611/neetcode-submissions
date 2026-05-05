class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        print(res)
        
        for index,temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([temperature,index])
                continue
                #[0] -> numero
                #[1] -> indice
        
            # ciclo para eliminar los menores
            while len(stack) > 0:
                if temperature > stack[-1][0]:
                    # actualizar resultados
                    res[stack[-1][1]] = index - stack[-1][1]
                    stack.pop()
                    continue
                break
            stack.append([temperature,index])

        return res