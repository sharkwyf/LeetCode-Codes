#include "LeetCode.h"


class Solution {
public:
	static int shifts[4][2];

public:
	vector<vector<int>> generateMatrix(int n) {
		vector<vector<int>> res(n, vector<int>());//³õÊ¼²ãÊý£¬¸³Öµ
		for (int i = 0; i < n; i++) {
			res[i].resize(n);
		}
		int i = 0, j = -1, d = 0;
		for (int c = 0; c < n * n; c++) {
			int mi = i + shifts[d][0], mj = j + shifts[d][1];
			if (!(0 <= mi && mi < n && 0 <= mj && mj < n && res[mi][mj] == 0)) {
				d = (d + 1) % 4;
				i = i + shifts[d][0], j = j + shifts[d][1];
			}
			else
				i = mi, j = mj;
			res[i][j] = c + 1;
		}
		return res;
	}
};

int Solution::shifts[4][2] = {
	{0, 1}, {1, 0}, {0, -1}, {-1, 0}
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

	vector<vector<int>> res = s.generateMatrix(3);

	return 0;
}

