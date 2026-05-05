class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // definir vector de mapas, mapa temporal y vector a retornar
        vector<unordered_map<char,int>> umaps;
        unordered_map<char,int> tmap;
        vector<vector<string>> anagrams;
        bool found;

        // loop para iterar sobre cada elemento de strs y mapearlo en el hashmap
        for(int i = 0; i < strs.size(); i++){

            //limpiar map
            tmap.clear();

            // loop para iterar sobre cada caracter en el string
            for(int x = 0; x < strs[i].length(); x++){
                // hashear en temp map
                tmap[strs[i][x]] += 1;
            }
            // una vez salido del bucle...
            // si es el primer elemento se inserta directamente
            if(i == 0){
                // insertar en vector
                anagrams.push_back({});
                anagrams[0].push_back(strs[i]);

                // insertar en el hash principal
                umaps.push_back({});
                umaps[0] = tmap;
            }else{
                // si no es el primer elemento comparar a ver si ya lo tenemos en el hashmap
                // recorrer todos los elementos en el diccionario
                for(int z =0; z < umaps.size(); z++){
                    found = false;
                    if(tmap == umaps[z]){
                        // si lo encontro pushearlo en el vector pero no en el hash
                        anagrams[z].push_back(strs[i]);
                        found = true;
                        break;
                    }
                }

                if(found == false){
                    // si no lo encontro entonces insertamos en vector y pusheamos en hash
                    // insertar en vector
                    anagrams.push_back({});
                    anagrams[anagrams.size() - 1].push_back(strs[i]);

                    // insertar en el hash principal
                    umaps.push_back({});
                    umaps[umaps.size() -1 ] = tmap;
                }
            }
        }
        return anagrams;
    }
};
