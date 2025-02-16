#include <bits/stdc++.h>
using namespace std;
int n, x;
struct cmp {
    bool operator() (int a, int b){
        if(abs(a) == abs(b)){
            return a > b;
        }
        return abs(a) > abs(b);
    }
};
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    priority_queue<int, vector<int>, cmp> pq;
    cin >> n;
    while (n--)
    {
        cin >> x;
        if (x == 0)
        {
            if (pq.empty())
            {
                cout << 0 << "\n";
            }
            else
            {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
        {
            pq.push(x);
        }
    }
}
// 이 문제는 자료구조의 활용 문제이다. 
// 난 Priority_Queue를 사용했고, 비교 알고리즘은 절대값의 크기를 사용했다.
// 다른 언어에서는 모르겠지만, C++에서는 compare struct를 만드는게 요점이였던거 같다.