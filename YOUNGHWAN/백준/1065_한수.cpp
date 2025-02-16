#include <bits/stdc++.h>
using namespace std;
int n;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        if (i < 100)
        {
            cnt++;
        }
        else if (i < 1000)
        {
            int a = i / 100;
            int b = (i % 100) / 10;
            int c = i % 10;
            if (a - b == b - c)
            {
                cnt++;
            }
        }
    }
    cout << cnt;
}
// 1.알고리즘 : 완전 탐색으로 품. 입력값이 크지 않고, 문제도 어렵지 않아 완전탐색 선택.
// 100 미만은 무조건 매자리가 등차, 100 이상은 자릿수 쪼개서 똑같은지 확인.