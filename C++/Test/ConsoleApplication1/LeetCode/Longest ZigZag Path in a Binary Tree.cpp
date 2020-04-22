#include "LeetCode.h"



class Solution {
public:
	int shipWithinDays(vector<int>& weights, int D) {
		int m = *max_element(weights.begin(), weights.end());
		int len = weights.size();
		if (len <= D)
			return m;
		vector<int> pos(D);
		vector<int> sums(D);
		for (int i = 0; i < D; i++) {
			pos[i] = i;
			if (i < D - 1) {
				sums[i] = weights[i];
			}
			else {
				sums[i] = 0;
				for (int j = i; j < len; j++)
					sums[i] += weights[j];
			}
		}
		while (true) {
			int mm = sums[D - 1];
			for (int i = 0; i < D - 1; i++) {
				while (pos[i + 1] < len) {
					if (sums[i] + weights[pos[i + 1]] <= m) {
						sums[i] += weights[pos[i + 1]];
						sums[i + 1] -= weights[pos[i + 1]];
						pos[i + 1]++;
					}
					else {
						mm = min(mm, sums[i] + weights[pos[i + 1]]);
						break;
					}
				}
				if (sums[i + 1] < 0) {
					sums[i + 1] = 0;
					pos[i + 1] = pos[i];
				}
			}
			if (sums[D - 1] <= m)
				return m;
			else
				m = mm;
		}
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{1,2,3,4,5,6,7,8,9,10}
	};
	vector<int> vv2 = {
		{ -1, -1, -1, -1 }
	};

	int res = s.shipWithinDays(vv1, 5);

	return 0;
}

