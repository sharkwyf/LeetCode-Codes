#include "LeetCode.h"


class Solution {
public:
	int openLock(vector<string>& deadends, string target) {
		vector<string> visited = deadends;
		queue<string> q;
		int step = 0;
		q.push(target);
		while (!q.empty()) {
			step++;
			for (int i; i < q.size(); i++) {
				string s = q.front();
				q.pop();
				for (int digit = 0; digit < 4; digit++) {
					string s1 = s, s2 = s;
					s1[i] = (s1[i] == '9' ? '0' : s1[i] + 1);
					s2[i] = (s2[i] == '0' ? '9' : s2[i] - 1);
					if (s1 == target || s2 == target)
						return step;
					q.push(s1);
					q.push(s2);
				}

			}
		}
		return 0;
	}
};


int main()
{

	Solution s;
	vector<string> v = {
		{ "0201", "0101", "0102", "1212", "2002" }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	int res = s.openLock(v, "0202");

	return 0;
}

