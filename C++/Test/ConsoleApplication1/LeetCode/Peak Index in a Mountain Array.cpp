#include "LeetCode.h"


class Solution {
public:
	int peakIndexInMountainArray(vector<int>& A) {
		int l = 0, r = A.size() - 1;
		while (l + 1 < r) {
			int mid = (l + r) / 2;
			if (A[mid] > A[mid + 1]) {
				r = mid;
			}
			else {
				l = mid + 1;
			}
		}
		return l;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{3,9,20,15,7}
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

	int res = s.peakIndexInMountainArray(vv1);

	return 0;
}

