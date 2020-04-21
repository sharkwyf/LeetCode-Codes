#include "LeetCode.h"


class Solution {
public:
	int triangleNumber(vector<int>& nums) {
		int len = nums.size();
		sort(nums.begin(), nums.end());
		int v = len;
		for (int i = 0; i < len; i++) {
			if (nums[i] > 0) {
				v = i;
				break;
			}
		}
		int cnt = 0;
		for (int i = v; i < len - 2; i++) {
			int r = i + 2;
			for (int j = i + 1; j < len - 1; j++) {
				while (r < len && nums[r] < nums[i] + nums[j]) {
					r++;
				}
				cnt += r - j - 1;
			}
		}
		return cnt;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = {
		{ 0, 1, 1, 0, 2 }
	};
	vector<int> v2 = {
		 { 1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.triangleNumber(v1);

	return 0;
}

