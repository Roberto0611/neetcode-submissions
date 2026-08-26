class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # valores iniciales
        sum_actual = 0
        history = {}
        history[0] = 1 # inicializar en 1 para edgecases
        output = 0

        for i in nums:
            sum_actual += i

            output += history.get(sum_actual - k, 0) # si no esta en el mapa sumar 0

            history[sum_actual] = history.get(sum_actual,0) + 1
        return output
