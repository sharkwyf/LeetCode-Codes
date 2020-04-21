#include "LeetCode.h"


class MyStack {
public:
	queue<int> q1, q2;
	bool in1 = true;

	/** Initialize your data structure here. */
	MyStack() {

	}

	/** Push element x onto stack. */
	void push(int x) {
		if (in1)
			q1.push(x);
		else
			q2.push(x);
	}

	/** Removes the element on top of the stack and returns that element. */
	int pop() {
		queue<int> *p1 = in1 ? &q1 : &q2, *p2 = in1 ? &q2 : &q1;
		int len = p1->size();
		for (int i = 0; i < len - 1; i++) {
			p2->push(p1->front());
			p1->pop();
		}
		int res = p1->front();
		p1->pop();
		in1 = !in1;
		return res;
	}

	/** Get the top element. */
	int top() {
		if (in1)
			return q1.back();
		else
			return q2.back();
	}

	/** Returns whether the stack is empty. */
	bool empty() {
		return in1 ? q1.empty() : q2.empty();
	}
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */


int main()
{
	MyStack stack = MyStack();

	stack.push(1);
	stack.push(2);
	stack.top();   // returns 2
	stack.pop();   // returns 2
	stack.empty(); // returns false

	//Solution s;
	//vector<int> v1 = {
	//	{1,2,4,16,8,4}
	//};
	//vector<int> v2 = {
	//	 { 1 }
	//};
	//vector<vector<int>> vv = {
	//	{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	//};

	//bool res = s.canReorderDoubled(v1);

	return 0;
}

