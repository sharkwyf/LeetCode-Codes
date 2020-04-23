#include "LeetCode.h"


class Solution {
public:
	string decodeAtIndex(string S, int K) {
		int cnt = 0, len = S.length();
		for (int i = 0; i < len; i++) {
			if ('2' <= S[i] && S[i] <= '9') {
				int base = cnt;
				cnt *= S[i] - '0';
				if (cnt >= K) {
					int r = K % base;
					return decodeAtIndex(S, r == 0 ? base : r);
				}
			}
			else {
				cnt++;
				if (cnt == K)
					return S.substr(i, 1);
			}
		}
		return "";
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


	auto res = s.decodeAtIndex("a23", 6);

	return 0;
}

