#include "LeetCode.h"



class Solution {
public:
	bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
		vector<int> v(n, 0);
		for (int i = 0; i < n; i++) {
			if (leftChild[i] > -1)
				v[leftChild[i]]++;
			if (rightChild[i] > -1)
				v[rightChild[i]]++;
		}
		int root = -1;
		for (int i = 0; i < n; i++) {
			if (v[i] == 0) {
				if (root > -1)
					return false;
				else
					root = i;
			}
			else if (v[i] > 1)
				return false;
		}
		if (root == -1)
			return false;
		vector<int> stack = { root };
		int cnt = 0;
		while (!stack.empty()) {
			int node = stack.back();
			stack.pop_back();
			cnt++;
			if (leftChild[node] > -1)
				stack.push_back(leftChild[node]);
			if (rightChild[node] > -1)
				stack.push_back(rightChild[node]);
		}
		return cnt == n;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{ 1, 2, 0, -1 }
	};
	vector<int> vv2 = {
		{ -1, -1, -1, -1 }
	};

	bool res = s.validateBinaryTreeNodes(4, vv1, vv2);

	return 0;
}

