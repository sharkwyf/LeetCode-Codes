#include "LeetCode.h"


class Solution {
public:
	int uniqueMorseRepresentations(vector<string>& words) {
		string map[26] = { ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.." };
		set<string> S;
		for (string s : words) {
			string res = "";
			for (char c : s) {
				res += map[c - 'a'];
			}
			S.insert(res);
		}
		return S.size();
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
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
	//	nodes[i] = new ListNode(vv1[i]);
	//	if (i < size - 1)
	//		nodes[i]->next = nodes[i + 1];
	//}
#pragma endregion


	auto res = s.uniqueMorseRepresentations(vv1);

	return 0;
}

