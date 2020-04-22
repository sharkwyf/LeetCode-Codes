#include "LeetCode.h"


class Solution {
public:
	ListNode* removeZeroSumSublists(ListNode* head) {
		unordered_map<int, vector<ListNode*>> map;
		int s = 0;
		ListNode *cur = new ListNode(0);
		cur->next = head;
		head = cur;
		while (cur) {
			s += cur->val;
			if (!map[s].empty()) {
				for (auto p : map[s]) {
					p->next = cur->next;
				}
			}
			map[s].push_back(cur);
			cur = cur->next;
		}
		return head->next;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{1,3,2,-3,-2,5,5,-5,1}
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

#pragma region ListNode Inputs
	int size = vv1.size();
	vector<ListNode*> nodes(size);
	for (int i = size - 1; i >= 0; i--) {
		nodes[i] = new ListNode(vv1[i]);
		if (i < size - 1)
			nodes[i]->next = nodes[i + 1];
	}
#pragma endregion


	auto res = s.removeZeroSumSublists(nodes[0]);

	return 0;
}

