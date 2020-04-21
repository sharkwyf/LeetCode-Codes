#include "LeetCode.h"


class Solution {
public:
	void sortColors(vector<int>& nums) {
		int i = 0, j = nums.size() - 1;
		while (i < j) {
			if (nums[i] == 0)
				i++;
			else if (nums[j] == 0) {
				swap(nums, i, j);
			}
			else
				j--;
		}
		j = nums.size() - 1;
		while (i < j) {
			if (nums[i] == 1)
				i++;
			else if (nums[j] == 1) {
				swap(nums, i, j);
			}
			else
				j--;
		}
	}

	void swap(vector<int>& nums, int i, int j) {
		int tmp = nums[j];
		nums[j] = nums[i];
		nums[i] = tmp;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = {
		{2,0,2,1,1,0}
	};
	vector<int> v2 = {
		 { 1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	s.sortColors(v1);

	return 0;
}

