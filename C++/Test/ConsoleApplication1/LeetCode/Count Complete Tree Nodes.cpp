#include "LeetCode.h"


class Solution {
public:
	int countNodes(TreeNode* root) {
		int height = 0;
		TreeNode *cur = root;
		while (cur) {
			height++;
			cur = cur->left;
		}
		if (height < 2)
			return height;
		int nodes = helper(root, height);

		return pow(2, height - 1) - 1 + nodes;
	}

	int helper(TreeNode* root, int height) {
		if (height == 2) {
			if (!root->left)
				return 0;
			else if (!root->right)
				return 1;
			else
				return 2;
		}
		else {
			int h = 0;
			TreeNode *cur = root->left;
			while (cur) {
				h++;
				cur = cur->right;
			}
			if (h == height - 1) {
				return pow(2, height - 2) + helper(root->right, height - 1);
			}
			else {
				return helper(root->left, height - 1);
			}
		}
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		1,2,3,4
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
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

	TreeNode *r0 = new TreeNode(0 + 1);
	TreeNode *r1 = new TreeNode(1 + 1);
	TreeNode *r2 = new TreeNode(2 + 1);
	TreeNode *r3 = new TreeNode(3 + 1);
	TreeNode *r4 = new TreeNode(4 + 1);
	TreeNode *r5 = new TreeNode(5 + 1);
	//r0->left = r1;
	//r0->right = r2;
	r1->left = r3;
	r1->right = r4;
	r2->left = r5;



	auto res = s.countNodes(r0);
	return 0;
}

