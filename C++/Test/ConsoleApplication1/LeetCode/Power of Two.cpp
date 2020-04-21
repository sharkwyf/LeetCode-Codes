#include "LeetCode.h"


class Solution {
public:
	bool isPowerOfTwo(int n) {
		while (n > 1) {
			if (n % 2 == 1)
				return false;
			else
				n /= 2;
		}
		return true;
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

	bool res = s.isPowerOfTwo(1);

	return 0;
}

