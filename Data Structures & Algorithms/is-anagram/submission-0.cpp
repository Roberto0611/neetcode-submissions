class Solution {
public:
    bool isAnagram(string s, string t) {
        // crear mapas
    unordered_map<char,int> map1;
    unordered_map<char,int> map2;
    
    // mapa 1 
    for(int i = 0; i < s.length(); i++){
        map1[s[i]] += 1;
    }

    // mapa 2
    for(int i = 0; i < t.length(); i++){
        map2[t[i]] += 1;
    }

    return map1 == map2;
    }
};
