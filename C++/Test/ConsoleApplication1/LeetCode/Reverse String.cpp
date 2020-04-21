#include "LeetCode.h"

class Solution {
public:
	void reverseString(vector<char>& s) {
		int len = s.size();
		for (int i = 0; i < len / 2; i++) {
			swap(s[i], s[len - 1 - i]);
		}
	}
};


int main()
{
	Solution s;
	vector<char> v1 = 
		{ 'h','e','l','l','o' }
	;
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	s.reverseString(v1);

	return 0;
}

