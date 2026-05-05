class Solution {
public:

    string encode(vector<string>& strs) {
        string resultante;
        for(int i = 0; i < strs.size(); i++){
            resultante = resultante + strs[i] + "🤑";
        }
        return resultante;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string delimiter = "🤑";

        // loop
        while(true)
        {
            int pos = s.find(delimiter);

            if(pos == -1){
                break;
            }

            result.push_back(s.substr(0,pos));
            s.erase(0,pos + delimiter.length());        
        }

        return result;
    }
};
