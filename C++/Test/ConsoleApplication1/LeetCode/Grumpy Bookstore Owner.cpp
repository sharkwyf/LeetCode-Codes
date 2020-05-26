#include "LeetCode.h"


class Solution {
public:
	int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
		
		int len = customers.size();
		int s = 0, res = 0;
		for (int i = 0; i < X; i++) {
			s += (1 - grumpy[i]) * customers[i];
			res += grumpy[i] * customers[i];
		}
		int m = res;
		for (int i = 0; i < len - X; i++) {
			s += (1 - grumpy[i + X]) * customers[i + X];
			res = res + grumpy[i + X] * customers[i + X] - grumpy[i] * customers[i];
			m = max(m, res);
		}
		return s + m;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,0,1,2,1,1,7,5
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

	auto res = s.maxSatisfied(vv1, vv2 ,3);
 

	return 0;
}

