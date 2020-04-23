#include "LeetCode.h"


class Solution {
public:
	int longestPalindrome(string s) {
		bool arr[52] = {};
		int cnt = 0;
		for (char c : s) {
			int id = (c >= 'a') ? (c - 'a') : (c - 'A' + 26);
			if (arr[id]) {
				cnt += 2;
				arr[id] = false;
			}
			else {
				arr[id] = true;
			}
		}
		return cnt + (s.length() > cnt ? 1 : 0);
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


	auto res = s.longestPalindrome("AAabccccdd");
	res = s.longestPalindrome("AAabccccdd");
	res = s.longestPalindrome("AAabccccdd");

	return 0;
}

