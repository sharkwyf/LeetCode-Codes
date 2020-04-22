#include "LeetCode.h"


class Solution {
public:
	TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		return helper(preorder.begin(), preorder.end(), inorder.begin(), inorder.end());
	}

	TreeNode* helper(
		vector<int>::iterator pbegin, 
		vector<int>::iterator pend,
		vector<int>::iterator ibegin,
		vector<int>::iterator iend
		) {
		if (pbegin == pend)
			return NULL;
		else {
			TreeNode *node = new TreeNode(*pbegin);
			int i = 0;
			for (auto it = ibegin; *it != *pbegin; it++) i++;

			node->left = helper(pbegin + 1, pbegin + 1 + i, ibegin, ibegin + i);
			node->right = helper(pbegin + 1 + i, pend, ibegin + i + 1, iend);
			return node;
		}
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv1 = {
		{3,9,20,15,7}
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

	TreeNode* res = s.buildTree(vv1, vv2);

	return 0;
}

