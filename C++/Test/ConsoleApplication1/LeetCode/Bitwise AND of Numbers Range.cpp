#include "LeetCode.h"


class Solution {
public:
	int rangeBitwiseAnd(int m, int n) {
		unsigned range = unsigned(n) - m + 1;
		if (range == 1) {
			return m;
		}
		int res = 0, base = 1;
		while (m > 0) {
			int a = m & 1 & n;
			if (range <= base && (m & 1 & n) == 1) {
				res += base;
			}
			base <<= 1;;
			m >>= 1;
			n >>= 1;
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


	auto res = s.rangeBitwiseAnd(6, 7);
	return 0;
}

