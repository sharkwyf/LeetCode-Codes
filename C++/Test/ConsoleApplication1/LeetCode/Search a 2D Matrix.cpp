#include "LeetCode.h"


class Solution {
public:
	bool searchMatrix(vector<vector<int>>& matrix, int target) {
		int height = matrix.size();
		if (!height)
			return false;
		int width = matrix[0].size();
		if (!width)
			return false;
		if (height == 1 && matrix[0][0] > target)
			return false;
		int l = 0, r = height;
		while (l < r) {
			int mid = l + (r - l + 1) / 2;
			if (matrix[mid][0] == target)
				return true;
			else if (matrix[mid][0] > target) {
				r = mid - 1;
			}
			else {
				l = mid;
			}
		}
		int row = l;
		if (width == 1 && matrix[row][0] != target)
			return false;
		l = 0, r = width;
		while (l < r) {
			int mid = l + (r - l + 1) / 2;
			if (matrix[row][mid] == target)
				return true;
			else if (matrix[row][mid] > target) {
				r = mid - 1;
			}
			else {
				l = mid;
			}
		}
		return false;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = {
		{1}
	};
	vector<int> vv1 = {
		1,2,3,4
	};
	vector<int> vv2 = {
		0,1,0,1,0,1,0,1
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

	auto res = s.searchMatrix(v1, 1);

	return 0;
}

