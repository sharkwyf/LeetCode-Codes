#include "LeetCode.h"


class Solution {
public:
	int numberOfSubstrings(string s) {
		int arr[3] = { 0, 0, 0 };
		int l = 0, r = 0;
		int len = s.length();
		int res = 0;
		while (r < len) {
			arr[s[r++] - 'a'] += 1;
			if (arr[0] > 0 && arr[1] > 0 && arr[2] > 0){
				while (arr[s[l] - 'a'] > 1) {
					arr[s[l] - 'a']--;
					l++;
				}
				res += l + 1;
			}
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,0,1,2,1,1,7,5
	};
	vector<int> vv2 = {
		0,1,0,1,0,1,0,1
	};

#pragma region ListNode Inputs
	//int size = vv1.size();
	//vector<ListNode*> nodes(size);
	//for (int i = size - 1; i >= 0; i--) {
	//	nodes{i] = new ListNode(vv1[i]);
	//	if (i < size - 1)
	//		nodes[i]->next = nodes[i + 1];
	//}
#pragma endregion

	auto res = s.numberOfSubstrings("aaabc");

	return 0;
}

