#include "LeetCode.h"


 
class Solution {
public:
	vector<int> nextLargerNodes(ListNode* head) {
		vector<int> res;
		unordered_map<int, ListNode*> dict;
		unordered_map<int, ListNode*>::iterator it;
		int last = 0;
		int index = 0;
		while (head != NULL && head->val > 0) {
			res.push_back(0);
			if (last < head->val) {
				vector<int> keys;
				for (it = dict.begin(); it != dict.end(); it++) {
					keys.push_back(it->first);
				}
				for (int k : keys) {
					ListNode *p = dict[k];
					int id = k;
					while (p != head && res[k] == 0) {
						if (p->val < head->val)
						{
							res[k] = head->val;
						}
						p = p->next;
						k++;
					}
					if (dict[id]->val < head->val)
						dict.erase(id);
				}
				dict[index] = head;
			}

			last = head->val;
			head = head->next;
			index++;
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv = {
		{3,2,5,4,6,1,7,0}
	};

	ListNode *head = new ListNode(-1),
		*n0 = new ListNode(2),
		n1 = ListNode(1),
		n2 = ListNode(5),
		n3 = ListNode(3),
		n4 = ListNode(5),
		n5 = ListNode(0);
	n0->next = &n1;
	n1.next = &n2;
	//n2.next = &n5;
	//n2.next = &n3;
	n3.next = &n4;
	n4.next = &n5;


	vector<int> res = s.nextLargerNodes(n0);

	return 0;
}

