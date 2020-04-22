#include "LeetCode.h"


class Solution {
public:
	vector<int> numMovesStonesII(vector<int>& stones) {
		int N = stones.size();
		sort(stones.begin(), stones.end());
		int j = 0;
		int lres = INT32_MAX;
		for (int i = 0; i < N; i++) {
			if (stones[i] + N - 1 > stones[N - 1])
				break;
			while (j < N && stones[j] < stones[i] + N) {
				j++;
			}
			if (i == 0 && j == N - 1)
				lres = min(lres, 2);
			else
				lres = min(lres, N - j + i);
		}
		int hres = 0;
		if (stones[1] + N - 2 != stones[N - 1]) {
			hres = max(hres, stones[N - 1] - (N - 1) - stones[1] + 1);
		}
		if (stones[0] + N - 2 != stones[N - 2]) {
			hres = max(hres, stones[N - 2] - (stones[0] + N - 1) + 1);
		}
		return { lres, hres };
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{6,5,4,3,10}
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

#pragma region ListNode Inputs
	//int size = vv1.size();
	//vector<ListNode*> nodes(size);
	//for (int i = size - 1; i >= 0; i--) {
	//	nodes[i] = new ListNode(vv1[i]);
	//	if (i < size - 1)
	//		nodes[i]->next = nodes[i + 1];
	//}
#pragma endregion


	auto res = s.numMovesStonesII(vv1);

	return 0;
}

