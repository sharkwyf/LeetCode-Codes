#include "LeetCode.h"


class Solution {
public:
	int maxSumDivThree(vector<int>& nums) {
		vector<int> arr(6, 10001);
		int res = 0;
		for (int n : nums) {
			res += n;
			if (n % 3 == 1) {
				arr[2] = n;
				sort(arr.begin(), arr.begin() + 3);
			}
			else if (n % 3 == 2) {
				arr[5] = n;
				sort(arr.begin() + 3, arr.end());
			}
		}
		if (res % 3 == 1)
			res -= min(arr[0], arr[3] + arr[4]);
		else if (res % 3 == 2) {
			res -= min(arr[0] + arr[1], arr[3]);
		}
		return res;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		4
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

	auto res = s.maxSumDivThree(vv1);
	return 0;
}

