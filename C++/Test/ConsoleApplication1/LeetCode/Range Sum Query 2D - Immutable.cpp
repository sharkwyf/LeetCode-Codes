#include "LeetCode.h"


class NumMatrix {
protected:
	vector<vector<int>> sums;

public:
	NumMatrix(vector<vector<int>>& matrix) {
		int h = matrix.size();
		if (h == 0)
			return;
		int w = matrix[0].size();
		vector<int> row(w + 1, 0);
		sums.push_back(row);
		for (int i = 0; i < h; i++) {
			row = { 0 };
			for (int j = 1; j < w + 1; j++) {
				row.push_back(row[j - 1] + sums[i][j] - sums[i][j - 1] + matrix[i][j - 1]);
			}
			sums.push_back(row);
		}
	}

	int sumRegion(int row1, int col1, int row2, int col2) {
		int a = sums[row2 + 1][col2 + 1];
		int b = sums[row1 + 1][col1 + 1];
		int c = sums[row1 + 1][col2 + 1];
		int d = sums[row2 + 1][col1 + 1];
		return sums[row2 + 1][col2 + 1] + sums[row1][col1]
			- sums[row1][col2 + 1] - sums[row2 + 1][col1];
	}
};


int main()
{
	//Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		-3,2,-3,4,2
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

#pragma region ListNode Inputs
	//int size = vv1.size();
	//vector<ListNode*> nodes(size);
	//for (int i = size - 1; i >= 0; i--) {
	//	nodes{i] = new ListNode(vv1[i]);
	//	if (i < size - 1)
	//		nodes[i]->next = nodes[i + 1];
	//}
#pragma endregion


	//auto res = s.longestPalindrome("AAabccccdd");


	NumMatrix* obj = new NumMatrix(v1);
	int param_1 = obj->sumRegion(2, 1, 4, 3);
	return 0;
}

