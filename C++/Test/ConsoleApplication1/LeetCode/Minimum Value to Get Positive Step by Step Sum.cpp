#include "LeetCode.h"


class Solution {
public:
	int minStartValue(vector<int>& nums) {
		int cnt = 0, m = 1;
		for (auto n : nums) {
			cnt += n;
			if (cnt < m)
				m = cnt;
		}
		return 1 - m;
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


	auto res = s.minStartValue(vv1);

	return 0;
}

