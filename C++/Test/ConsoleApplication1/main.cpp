#include "LeetCode.h"


class Solution {
public:
	int maxScoreSightseeingPair(vector<int>& A) {
		int m = 0, res = 0;
		for (int i = 0; i < A.size(); i++) {
			res = max(res, m + A[i] - i);
			m = max(m, A[i] + i);
		}
		return res;
	}
};


int main()
{

	Solution s;
	vector<int> v = {
		{ 8,1,5,2,6 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.maxScoreSightseeingPair(v);

	return 0;
}

