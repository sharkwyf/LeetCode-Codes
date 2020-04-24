#include "LeetCode.h"


class Solution {
public:
	bool isPossibleDivide(vector<int>& nums, int k) {
		map<int, int> d;
		for (int n : nums) {
			d[n]++;
		}
		for (auto it = d.begin(); it != d.end(); it++) {
			if (it->second > 0) {
				for (int i = 1; i < k; i++) {
					if (d[it->first + i] < it->second)
						return false;
					d[it->first + i] -= it->second;
				}
			}
		}
		return true;
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


	auto res = s.isPossibleDivide(vv1, 3);
	return 0;
}

