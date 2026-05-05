class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // crear mapa
        unordered_map<int,int> umap;
        int expected;

        // ciclo 1
        for(int i = 0; i < nums.size(); i++){
            expected = target - nums[i];


            // recorrer mapa para saber si encontramos el numero
            for(auto x : umap){
                // cout << "Comparando " << x.first << " y " << expected << endl;
                if(x.first == expected){
                    return {x.second,i};
                }
            }

            // en caso de no hacer el return hacer un append al diccionario
            umap[nums[i]] = i;


        }
        return {};
    }
};
