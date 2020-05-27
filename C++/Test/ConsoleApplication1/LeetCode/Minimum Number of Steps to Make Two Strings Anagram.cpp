#include "LeetCode.h"


class Solution {
public:
	int minSteps(string s, string t) {
		int cnt[26]{ 0 };
		int res = 0;
		for (char c : s) {
			cnt[c - 'a']++;
		}
		for (char c : t) {
			cnt[c - 'a']--;
		}
		for (int i : cnt)
			if (i > 0)
				res += i;
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { 
		{1}
	};
	vector<int> vv1 = {
		3,5,7
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

	auto res = s.minSteps("leetcode", "practice");
	return 0;
}

