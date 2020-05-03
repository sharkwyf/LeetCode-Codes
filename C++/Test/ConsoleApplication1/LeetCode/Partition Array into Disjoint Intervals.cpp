#include "LeetCode.h"


class Solution {
public:
	int partitionDisjoint(vector<int>& A) {
		int len = A.size();
		int* maxs = new int[len] {0};
		int* mins = new int[len] {0};
		int m = 0;
		for (int i = 0; i < len; i++) {
			m = max(m, A[i]);
			maxs[i] = m;
		}
		m = INT32_MAX;
		for (int i = len - 1; i > 0; i--) {
			m = min(m, A[i]);
			mins[i] = m;
		}
		for (int i = 0; i < len - 1; i++) {
			if (maxs[i] < mins[i + 1])
				return i + 1;
		}
		return 0;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,1,1,0,6,12
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

	auto res = s.partitionDisjoint(vv1);
	return 0;
}

