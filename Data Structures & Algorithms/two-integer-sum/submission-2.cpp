class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // puntero 1
        for(int i = 0; i < nums.size(); i++){
            //puntero 2
            for(int x = nums.size() - 1; x > 0; x--){
                if(nums[i] + nums[x] == target && i != x){
                    vector<int> result = {i, x};
                    return result;
                }
            }
        }
    }
};
