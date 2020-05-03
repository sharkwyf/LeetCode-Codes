#include "LeetCode.h"


class Solution {
public:
	bool find132pattern(vector<int>& nums) {
		int len = nums.size();
		vector<int> st = { INT32_MAX };
		int exp = INT32_MIN;
		for (int i = len - 1; i >= 0; i--) {
			if (nums[i] < exp)
				return true;
			if (nums[i] < st.back())
				st.push_back(nums[i]);
			else {
				while (st.back() < nums[i]) {
					exp = max(exp, st.back());
					st.pop_back();
					i++;
				}
			}
		}
		return false;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
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

	auto res = s.find132pattern(vv1);

	return 0;
}

