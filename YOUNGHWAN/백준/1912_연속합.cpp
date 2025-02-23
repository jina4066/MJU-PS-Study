#include <bits/stdc++.h>
#define MAX 1000000
using namespace std;
int k, ret;
int arr[MAX], dp[MAX];
int Max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    return b;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ret = -1004;
    cin >> k;
    for (int i = 1; i <= k; i++)
    {
        cin >> arr[i];
    }
    dp[1] = arr[1];
    ret = dp[1];
    for (int i = 2; i <= k; i++)
    {
        dp[i] = Max(arr[i], dp[i - 1] + arr[i]);
        ret = Max(ret, dp[i]);
    }
    cout << ret;
}