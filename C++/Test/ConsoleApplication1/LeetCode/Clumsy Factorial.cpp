#include "LeetCode.h"


class Solution {
public:
	int clumsy(int N) {
		int res = 0;
		if (N > 2) {
			res += N * (N - 1) / (N - 2);
			N -= 3;
		}
		while (N > 3) {
			res += N - (N - 1) * (N - 2) / (N - 3);
			N -= 4;
		}
		res += N > 0 ? 1 : 0;
		return res;
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

	int res = s.clumsy(4);

	return 0;
}

