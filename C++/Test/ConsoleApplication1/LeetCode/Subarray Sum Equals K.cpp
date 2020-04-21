#include "LeetCode.h"


class Solution {
public:
	int subarraySum(vector<int>& nums, int k) {
		unordered_map<int, int> dict;
		int s = 0, res = 0;
		dict[0] = 1;
		for (int n : nums) {
			s += n;
			res += dict[s - k];
			dict[s]++;
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = {
		{1, 1, 1}
	};
	vector<int> v2 = {
		 { 1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.subarraySum(v1, 2);

	return 0;
}

