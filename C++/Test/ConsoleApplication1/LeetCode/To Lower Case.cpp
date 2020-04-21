#include "LeetCode.h"

class Solution {
public:
	string toLowerCase(string str) {
		int len = str.length();
		int shift = 'A' - 'a';
		for (int i = 0; i < len; i++) {
			if ('A' <= str[i] && str[i] <= 'Z')
				str[i] -= shift;
		}
		return str;
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

	string res = s.toLowerCase("Hello");

	return 0;
}

