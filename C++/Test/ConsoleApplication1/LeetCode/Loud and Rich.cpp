#include "LeetCode.h"

class Solution {
public:
	vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
		int len = quiet.size();
		vector<vector<int>> G(len);
		vector<int> res(len);
		for (int i = 0; i < len; i++){
			res[i] = i;
		}
		vector<int> stack;
		for (vector<int> rich : richer) {
			int i = rich[0], j = rich[1];
			G[i].push_back(j);
			if (quiet[res[i]] < quiet[res[j]]) {
				stack.push_back(j);
				while (!stack.empty()) {
					int node = stack.back();
					stack.pop_back();
					if (quiet[res[i]] < quiet[res[node]])
						res[node] = res[i];
					for (int k : G[node]) {
						if (quiet[res[i]] < quiet[res[k]])
							stack.push_back(k);
					}
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
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv = {
		{3,2,5,4,6,1,7,0}
	};

	vector<int> res = s.loudAndRich(v1, vv);

	return 0;
}

