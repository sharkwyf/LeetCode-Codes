#include "LeetCode.h"


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
	vector<int> nextLargerNodes(ListNode* head) {
		vector<int> res;
		unordered_map<int, ListNode*> dict;
		unordered_map<int, ListNode*>::iterator it;
		int last = 0;
		while (head->val > 0) {
			res.push_back(0);
			if (last >= head->val) {

			}
			else {
				vector<int> keys;
				for (it = dict.begin(); it != dict.end(); it++) {
					keys.push_back(it->first);
				}
				for (int k : keys) {
					ListNode *p = dict[k];
					while (res[p->val] == 0) {
						if (p->val)
						{

						}
						k++;
					}
				}
			}

			last = head->val;
			head = head->next;
		}

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

	vector<int> res = s.loudAndRich(v1, vv);

	return 0;
}

