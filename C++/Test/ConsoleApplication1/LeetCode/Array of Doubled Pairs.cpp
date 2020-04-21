#include "LeetCode.h"


class Solution {
public:
	bool canReorderDoubled(vector<int>& A) {
		unordered_map<int, int> dict;
		for (int n : A) {
			dict[n] += 1;
		}
		vector<int> keys;
		unordered_map<int, int>::iterator it;
		for (it = dict.begin(); it != dict.end(); it++) {
			keys.push_back(it->first);
		}
		sort(keys.begin(), keys.end(), [](int x, int y) { return abs(x) < abs(y); });
		for (int key : keys) {
			if (dict[key] > dict[key * 2])
				return false;
			dict[key * 2] -= dict[key];
		}
		return true;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = {
		{1,2,4,16,8,4}
	};
	vector<int> v2 = {
		 { 1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	bool res = s.canReorderDoubled(v1);

	return 0;
}

