#include "LeetCode.h"


class Solution {
public:
	int magicalString(int n) {
		string S = "122";
		int i = 2;
		while (S.size() < n) {
			S += string(S[i++] - '0', '3' - S.back() + '0');
		}
		return count(S.begin(), S.begin() + n, '1');
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,0,1,2,1,1,7,5
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

	auto res = s.magicalString(4);

	return 0;
}

