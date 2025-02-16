#include <bits/stdc++.h>
using namespace std;
int n, m, t;
int min(int a, int b)
{
    if (a > b)
    {
        return b;
    }
    return a;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    int a[104] = {
        0,
    };

    for (int i = 0; i < m; i++)
    {
        cin >> t;
        a[t]++;
    }
    int last = 0, ink = 0;

    for (int i = 1; i <= n; i++)
    {
        if (!a[i])
        {
            if (last)
            {
                ink += min(7, (i - last) * 2);
            }
            else
            {
                ink += 7;
            }
            last = i;
        }
    }
    cout << ink;
}
// 잉크의 최솟값을 구하기 위해 DP를 사용했다. 
// DP를 사용할 때 새로 작성하는 값은 7, 연달아 출력하는 잉크의 값은 (i-last) * 2로 두고, 최솟값을 찾아 더해주는 방식을 사용했다.