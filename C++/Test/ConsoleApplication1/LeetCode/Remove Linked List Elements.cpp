#include "LeetCode.h"


class Solution {
public:
	ListNode* removeElements(ListNode* head, int val) {
		ListNode* dummy = new ListNode(-1);
		ListNode* prev = dummy;
		while (head != NULL) {
			ListNode* next = head->next;
			if (head->val != val) {
				prev->next = head;
				prev = prev->next;
				prev->next = NULL;
			}
			head = next;
		}
		return dummy->next;
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
	int size = vv1.size();
	vector<ListNode*> nodes(size);
	for (int i = size - 1; i >= 0; i--) {
		nodes[i] = new ListNode(vv1[i]);
		if (i < size - 1)
			nodes[i]->next = nodes[i + 1];
	}
#pragma endregion


	auto res = s.removeElements(nodes[0], 4);

	return 0;
}

