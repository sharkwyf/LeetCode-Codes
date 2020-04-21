#include "LeetCode.h"


class Solution {
public:
	int pivotIndex(vector<int>& nums) {
		int sum = 0;
		for (int n : nums)
			sum += n;
		int length = nums.size();
		int left = 0;
		for (int i = 0; i < length; i++) {
			if (left == (sum - nums[i]) / 2.0)
				return i;
			else {
				left += nums[i];
			}
		}
		return -1;
	}
};


int main()
{
	Solution s;
	vector<int> v = {
		{1, 7, 3, 6, 5, 6}
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.pivotIndex(v);

	return 0;
}

