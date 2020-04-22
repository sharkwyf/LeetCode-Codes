#include "LeetCode.h"



class Solution {
public:
	int lastStoneWeight(vector<int>& stones) {
		int m = *max_element(stones.begin(), stones.end());
		vector<int> weights(m + 1, 0);
		for (int w : stones) weights[w]++;
		int last = 0;
		for (int i = m; i >= 0; i--) {
			if (weights[i] > 0) {
				if (last == 0) {
					last = weights[i] % 2 == 1 ? i : 0;
				}
				else {
					while (last >= i && weights[i] > 0) {
						last -= i;
						weights[i]--;
					}
					if (last < i) {
						weights[last]++;
						last = weights[i] % 2 == 1 ? i : 0;
					}
				}
			}
		}
		return last;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{ 9,10,4,5,7,1}
	};
	vector<int> vv2 = {
		{ -1, -1, -1, -1 }
	};

	int res = s.lastStoneWeight(vv1);

	return 0;
}

