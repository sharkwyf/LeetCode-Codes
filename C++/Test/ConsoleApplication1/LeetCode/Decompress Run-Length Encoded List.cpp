#include "LeetCode.h"


class Solution {
public:
	vector<int> decompressRLElist(vector<int>& nums) {
		int len = nums.size();
		vector<int> res;
		for (int i = 0; i < len / 2; i++) {
			int n = nums[i * 2 + 1];
			for (int j = 0; j < nums[i * 2]; j++) {
				res.push_back(n);
			}
		}
		return res;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,2,3,4
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

	auto res = s.decompressRLElist(vv1);
	return 0;
}

