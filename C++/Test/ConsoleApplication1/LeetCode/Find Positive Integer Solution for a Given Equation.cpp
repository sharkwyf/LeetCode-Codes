#include "LeetCode.h"

class CustomFunction {
public:
	int f(int x, int y) {
		return x + y;
	}
};


class Solution {
public:
	vector<vector<int>> findSolution(CustomFunction& customfunction, int z) {
		int x = 1000, y = 1;
		vector<vector<int>> res;
		while (x >= 1 && y <= 1000) {
			int r = customfunction.f(x, y);
			if (r == z) {
				res.push_back({ x, y });
				x--;
				y++;
			}
			else if (r > z) {
				x--;
			}
			else {
				y++;
			}
		}
		return res;
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

	CustomFunction a = CustomFunction();
	vector<vector<int>> res = s.findSolution(a, 5);

	return 0;
}

