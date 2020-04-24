#include "LeetCode.h"


class Solution {
public:
	vector<int> largestDivisibleSubset(vector<int>& nums) {
		int len = nums.size();
		sort(nums.begin(), nums.end());
		unordered_map<int, int> map;
		vector<int> pre(len, -1);
		int mi = 0;
		for (int i = 0; i < len - 1; i++) {
			for (int j = i + 1; j < len; j++) {
				int l = nums[i], h = nums[j];
				if (h % l== 0) {
					if (map[l] + 1 > map[h]) {
						map[h] = map[l] + 1;
						pre[j] = i;
						if (map[h] > map[nums[mi]]) {
							mi = j;
						}
					}
				}
			}
		}
		vector<int> res;
		while (mi != -1) {
			res.push_back(nums[mi]);
			mi = pre[mi];
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
		3,5,7
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

	auto res = s.largestDivisibleSubset(vv1);
	return 0;
}

