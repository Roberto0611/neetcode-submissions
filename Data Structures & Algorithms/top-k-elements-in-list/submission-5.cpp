class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> umap;

        // loop para hashear el array
        for(int i = 0; i < nums.size(); i++){
            umap[nums[i]] += 1;
        }

        // vector resultado
        vector<int> resultado;
        vector<int> repeticiones;
        int min;

        // mostrar resultado
        for(auto it: umap){
            if (resultado.size() < k)
            {
                resultado.push_back(it.first);
                repeticiones.push_back(it.second);
            }else{
                // comparar con el valor minimo
                if(it.second > *min_element(repeticiones.begin(),repeticiones.end())){
                    int indexMin = min_element(repeticiones.begin(), repeticiones.end()) - repeticiones.begin();
                    resultado[indexMin] = it.first;
                    repeticiones[indexMin] = it.second;
                }
            }
        }

        return resultado;
    }
};
