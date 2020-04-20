#include "LeetCode.h"


class Solution {
public:
	string multiply(string num1, string num2) {
		string res = "0";
		int length = num2.length();
		for (int i = 0; i < length; i++) {
			res = multiplyX(num1, num2[length - 1 - i]);
		}
		return res;
	}

	string multiplyX(string num1, char num2) {
		int c = 0, n2 = num2 - '0';
		int length = num1.length();
		vector<char> res(length + 1);
		for (int i = 0; i < length; i++) {
			int r = (num1[length - 1 - i] - '0') * n2 + c;
			c = r / 10;
			res[length - i] = (r % 10) + '0';
		}
		if (c > 0)
			res[0] = c + '0';
		return res;
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

	string res = s.multiply("", "");

	return 0;
}

