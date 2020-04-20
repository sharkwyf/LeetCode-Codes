#include "LeetCode.h"


class Solution {
public:
	int openLock(vector<string>& deadends, string target) {
		unordered_set<string> visited(deadends.begin(), deadends.end());
		if (visited.find("0000") != visited.end())
			return -1;
		queue<string> q;
		int step = 0;
		q.push(target);
		while (!q.empty()) {
			step++;
			int size = q.size();
			for (int i = 0; i < size; i++) {
				string s = q.front();
				q.pop();
				for (int digit = 0; digit < 4; digit++) {
					string s1 = s, s2 = s;
					s1[digit] = (s1[digit] == '9' ? '0' : s1[digit] + 1);
					s2[digit] = (s2[digit] == '0' ? '9' : s2[digit] - 1);
					if (s1 == "0000" || s2 == "0000")
						return step;
					else {
						if (visited.find(s1) == visited.end()) {
							visited.insert(s1);
							q.push(s1);
						}
						if (visited.find(s2) == visited.end()) {
							visited.insert(s2);
							q.push(s2);
						}
					}
				}
			}
		}
		return -1;
	}
};


int main()
{
	Solution s;
	vector<string> v = {
		{ "8887","8889","8878","8898","8788","8988","7888","9888" }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.openLock(v, "8888");

	return 0;
}

