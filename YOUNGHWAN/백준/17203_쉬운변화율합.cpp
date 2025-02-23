#include <bits/stdc++.h>
using namespace std;
int n, q, a[1005], psum[1005];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> q;
    a[0] = 0;
    psum[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        psum[i] = psum[i - 1] + abs(a[i] - a[i - 1]);
    }
    int i, j;
    for (int k = 0; k < q; k++)
    {
        cin >> i >> j;
        if (i > j - 1)
        {
            cout << 0 << "\n";
            continue;
        }
        cout << psum[j] - psum[i] << "\n";
    }
    return 0;
}
// 1. 알고리즘 : 단순한 누적합 문제, 입력받는 i, j 구간의 변화율 합을 구하는 문제.
// 변화율 합을 psum(누적합 배열)에 저장한뒤, Slicing하는 간단한 문제이다.