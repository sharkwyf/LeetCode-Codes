#include <algorithm>;
#include <cmath>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>;
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};