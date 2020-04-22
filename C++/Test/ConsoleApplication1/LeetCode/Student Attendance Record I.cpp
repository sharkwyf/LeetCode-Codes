#include "LeetCode.h"


class Solution {
public:
	bool checkRecord(string s) {
		int A = 0, L = 0;
		for (char c : s) {
			if (A == 'L') {
				if (L == 2)
					return false;
				else
					L++;
			}
			else {
				if (A == 'A') {
					if (A == 1)
						return false;
					else
						A++;
				}
				L = 0;
			}
		}
		return true;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{3,9,20,15,7}
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

	bool res = s.checkRecord("PPALLL");

	return 0;
}

