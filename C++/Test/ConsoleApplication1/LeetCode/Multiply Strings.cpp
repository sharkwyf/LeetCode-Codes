#include "LeetCode.h"


class Solution {
public:
	string multiply(string num1, string num2) {
		string res = "0";
		int length = num2.length();
		for (int i = 0; i < length; i++) {
			string str = multiplyX(num1, num2[length - 1 - i]);
			if (str != "0")
				res = add(res, str.append(i, '0'));
		}
		return res;
	}

	string multiplyX(string num1, char num2) {
		if (num1 == "0" || num2 == '0')
			return "0";
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
		string s(res.begin() + (c > 0 ? 0 : 1), res.end());
		return s;
	}

	string add(string num1, string num2) {
		int len1 = num1.length(), len2 = num2.length();
		int length = max(len1, len2);
		vector<char> res(length + 1);
		bool c = false;
		for (int i = 0; i < length; i++) {
			int r = (len1 - 1 - i >= 0 ? num1[len1 - 1 - i] - '0' : 0) + (len2 - 1 - i >= 0 ? num2[len2 - 1 - i] - '0' : 0) + c;
			c = r > 9;
			res[length - i] = (r % 10) + '0';
		}
		if (c)
			res[0] = '1';
		string s(res.begin() + (c ?  0 : 1), res.end());
		return s;
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

	string res = s.multiply("123", "0");

	return 0;
}

