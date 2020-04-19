#include "LeetCode.h"


class Solution {
public:
	int countPrimeSetBits(int L, int R) {
		int cnt = 0;
		set<int> arr = { 2, 3, 5, 7, 11, 13, 17, 19 };
		for (int i = L; i <= R; i++) {
			int c = 0, v = i;
			while (v > 0) {
				c += v % 2;
				v = v / 2;
			}
			if (arr.count(c))
				cnt++;
		}
		return cnt;
	}
};

int main()
{

	Solution s;
	vector<int> v = {
		{ 8,1,5,2,6 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.countPrimeSetBits(10, 15);
	return 0;
}

