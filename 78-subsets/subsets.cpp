class Solution {
private: 
    void dfs(vector<int>& nums, int i, vector<int>& subset, vector<vector<int>>& result) {
        if (i == nums.size()) {
            result.push_back(subset);
            return;
        }
        subset.push_back(nums[i]);
        dfs(nums, i + 1, subset, result);
        subset.pop_back();
        dfs(nums, i + 1, subset, result);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<int> subset;
        std::vector<vector<int>> result;
        dfs(nums, 0, subset, result);
        return result;
    }
};