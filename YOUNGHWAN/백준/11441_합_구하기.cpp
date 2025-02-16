#include <bits/stdc++.h>
using namespace std;
int n, m, a[100005], i, j, psum[100005];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    psum[0] = 0;
    for (int k = 1; k <= n; k++)
    {
        cin >> a[k];
        psum[k] = psum[k - 1] + a[k];
    }
    cin >> m;
    for (int k = 1; k <= m; k++)
    {
        cin >> i >> j;
        cout << psum[j] - psum[i - 1] << "\n";
    }
}
// 알고리즘 : 전형적인 Prefix Sum 문제이다. 구간별 합을 출력하기에 Sliding Window 알고리즘도 함께 사용했다.
// 입력 받을 때 현재까지의 합을 psum배열에 같이 넣고 Sliding window는 i ~ j 까지의 누적합을 구하는데 사용하였다.