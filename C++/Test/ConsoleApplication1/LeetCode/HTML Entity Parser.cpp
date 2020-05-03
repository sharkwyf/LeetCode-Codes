#include "LeetCode.h"


class Solution {
public:
	string entityParser(string text) {
		int len = text.length();
		string sample[6] = { "gt;", "lt;", "amp;", "quot;", "apos;", "frasl;" };
		char sam[7] = "><&\"'/";
		char* res = new char[len + 1];
		int idx = 0;
		for (int i = 0; i < len; i++) {
			res[idx++] = text[i];
			if (text[i] == '&') {
				for (int m = 0; m < 6; m++) {
					int lens = sample[m].length();
					if (len - i > lens) {
						bool isSame = true;
						for (int j = 0; j < lens; j++) {
							if (text[i + j + 1] != sample[m][j]) {
								isSame = false;
								break;
							}
						}
						if (isSame) {
							res[idx - 1] = sam[m];
							i += lens;
						}
					}
					else
						break;
				}
			}
		}
		res[idx] = '\0';
		return res;
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

	auto res = s.entityParser("leetcode.com&frasl;problemset&frasl;all");
	return 0;
}

