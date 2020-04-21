#include "LeetCode.h"

class Solution {
public:
	vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
		vector<int> res(N, 1);
		unordered_map<int, vector<int>> dict;
		for (vector<int> path : paths) {
			int i = path[0] - 1, j = path[1] - 1;
			dict[i].push_back(j);
			dict[j].push_back(i);
			bool colors[] = { true, false, false, false, false};
			for (int k : dict[j]) {
				colors[res[k]] = true;
			}
			for (int m = 1; m < 5; m++) {
				if (colors[m] == false) {
					res[j] = m;
					break;
				}
			}
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 3}, {2, 4}}
	;
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	vector<int> res = s.gardenNoAdj(4, v1);

	return 0;
}

