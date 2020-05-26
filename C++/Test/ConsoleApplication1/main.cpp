#include "LeetCode.h"


class Solution {
public:
	int findPeakElement(vector<int>& nums) {
		int l = 0, r = nums.size() - 1;
		int lc = r * 0.382, rc = min(r, int(r * 0.618 + 1));
		while (l < r) {
			if (nums[lc] < nums[rc]) {
				l = lc;
				lc = rc;
				rc = min(int(l * 0.382 + r * 0.618 + 1), r);
			}
			else {
				r = rc;
				rc = lc;
				lc = l * 0.382 + r * 0.618;
			}
		}
		for (int i = l; i < r; i++)
			if (nums[i] > nums[i + 1])
				return i;
		return r;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { 
		{1}
	};
	vector<int> vv1 = {
		-19,59,97,2,-64,-31,-77,64,18,90,1,-44,81,-52,-20,93,-89,78,77,-42,27,3,-83,-49,99,75,-76,53,89,-14,4,44,57,39,-61,37,33,65,-3,60,-90,-16,36,-53,-69,52,-8,-58,26,8
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

	auto res = s.findPeakElement(vv1);
	return 0;
}

