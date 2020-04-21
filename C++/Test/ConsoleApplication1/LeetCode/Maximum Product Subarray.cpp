#include "LeetCode.h"


class Solution {
public:
	int maxProduct(vector<int>& nums) {
		int m = INT32_MIN;
		int p = 1, q = 1;
		for (int n : nums) {
			p *= n;
			q *= n;
			m = max(m,  p > q ? p : q);
			if (n > 0) {
				if (0 < p && p < 1)
					p = 1;
				if (0 < q && q < 1)
					q = 1;
			}
			else if (n == 0) {
				p = q = 1;
			}
			else {
				if (p > 0 && q > 0) {
					q = n;
				}
				else if (p < 0 && q < 0) {
					p = 1;
				}
			}
		}
		return m;
	}
};


int main()
{
	Solution s;
	vector<int> v = {
		{ -2,0,-1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.maxProduct(v);

	return 0;
}

