#include "LeetCode.h"


class Solution {
public:
	int shortestWay(string source, string target) {
		int lens = source.length(), lent = target.length();
		vector<vector<int>> pos(26);
		for (int i = 0; i < lens; i++) {
			pos[source[i] - 'a'].push_back(i);
		}
		int res = 0;
		for (int i = 0; i < lent;) {
			int m = 1;
			for (int j : pos[target[i] - 'a']) {
				int k = j, l;
				for (l = 1; j + l < lens && i + l < lent; l++) {
					if (source[j + l] != target[i + l])
						break;
				}
				m = max(m, l);
			}
			i += m;
			res++;
		}
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
		1,2,3,4
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

	auto res = s.shortestWay("xyz", "xzyxz");

	return 0;
}

