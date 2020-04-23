#include "LeetCode.h"


class Solution {
public:
	vector<int> circularPermutation(int n, int start) {
		int len = pow(2, n);
		int offset = (len - findPos(start)) % len;
		vector<int> res(len);
		res[(0 + offset) % len] = 0;
		res[(1 + offset) % len] = 1;
		for (int i = 1; i < n; i++) {
			int base = pow(2, i);
			for (int j = 0; j < pow(2, i); j++) {
				res[(base + j + offset) % len] = res[(base - 1 - j + offset) % len] + base;
			}
		}
		return res;
	}

	int findPos(int n) {
		if (n < 2)
			return n;
		else {
			int r = 1;
			while (r <= n) {
				r *= 2;
			}
			return r - 1 - findPos(n - r / 2);
		}
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 2, 2, 1},
		{3, 1, 2},
		{1, 3, 2},
		{2, 4},
		{3, 1, 2},
		{1, 3, 1, 1}}
	;
	vector<string> vv1 = {
		"gin", "zen", "gig", "msg"
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


	auto res = s.circularPermutation(3, 2);

	return 0;
}

