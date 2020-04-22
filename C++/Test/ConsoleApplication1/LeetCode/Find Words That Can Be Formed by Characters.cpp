#include "LeetCode.h"



class Solution {
public:
	int countCharacters(vector<string>& words, string chars) {
		unordered_map<int, int> map;
		int res = 0;
		for (char c : chars) {
			map[c]++;
		}
		for (string s : words) {
			auto mapC = unordered_map<int, int>(map);
			bool isIn = true;
			for (char c : s) {
				if (mapC[c] == 0) {
					isIn = false;
					break;
				}
				else
					mapC[c]--;
			}
			if (isIn)
				res += s.length();
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
	vector<string> vv1 = {
		{"cat","bt","hat","tree"}
	};
	vector<int> vv2 = {
		{ -1, -1, -1, -1 }
	};

	int res = s.countCharacters(vv1, "atach");

	return 0;
}

