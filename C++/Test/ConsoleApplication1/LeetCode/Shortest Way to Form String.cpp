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
			int j = 0;
			int lowbound = 0;
			while (i + j < lent) {
				auto p = pos[target[i + j] - 'a'];
				auto el = lower_bound(p.begin(), p.end(), lowbound);
				if (el == p.end()) {
					break;
				}
				else {
					lowbound = *el + 1;
					j++;
				}
			}
			if (j == 0)
				return -1;
			else {
				i += j;
				res++;
			}
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

	auto res = s.shortestWay("abc", "acdbc");

	return 0;
}

