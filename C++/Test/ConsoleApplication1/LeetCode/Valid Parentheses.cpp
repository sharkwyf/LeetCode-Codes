#include "LeetCode.h"


class Solution {
public:
	bool isValid(string s) {
		unordered_map<char, char> map = { {'(', ')'}, {'[', ']'}, {'{', '}'} };
		stack<char> st;
		for (char c : s) {
			if (c == '(' || c == '{' || c == '[')
				st.push(c);
			else {
				if (st.size() == 0 || map[st.top()] != c)
					return false;
				st.pop();
			}
		}
		return true;
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


	auto res = s.isValid("()[]{}");

	return 0;
}

