#include "LeetCode.h"


class Solution {
public:
	vector<int> numsSameConsecDiff(int N, int K) {
		vector<int> v = {};
		if (N == 1)
			return {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		for (int i = 1; i < 10; i++) {
			if ((0 <= i - K and i - K < 10) || (0 <= i + K and i + K < 10))
				v.push_back(i);
		}
		return nums(v, N - 1, K);
	}

private:
	vector<int> nums(vector<int> V, int N, int K) {
		if (N == 0)
			return V;
		else {
			vector<int> res = {};
			for (int i : V) {
				int x = i % 10 - K, y = i % 10 + K;
				if (0 <= x and x < 10)
					res.push_back(i * 10 + x);
				if (x != y and 0 <= y and y < 10)
					res.push_back(i * 10 + y);
			}
			return nums(res, N - 1, K);
		}
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

	vector<int> res = s.numsSameConsecDiff(2, 0);

	return 0;
}

