#include "LeetCode.h"


class Solution {
public:
	int leastBricks(vector<vector<int>>& wall) {
		unordered_map<int, int> map;
		for (auto row : wall) {
			int cnt = 0;
			int size = row.size();
			for (int i = 0; i < size - 1; i++) {
				cnt += row[i];
				map[cnt]++;
			}
		}
		int res = 0;
		for (auto it = map.begin(); it != map.end(); it++) {
			if (it->second > res)
				res = it->second;
		}
		return wall.size() - res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 2, 2, 1},
		{3, 1, 2},
		{1, 3, 2},
		{2, 4},
		{3, 1, 2},
		{1, 3, 1, 1}}
	;
	vector<string> vv1 = {
		"gin", "zen", "gig", "msg"
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


	auto res = s.leastBricks(v1);

	return 0;
}

