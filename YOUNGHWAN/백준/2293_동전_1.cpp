#include <bits/stdc++.h>
using namespace std;
int n, k;
int a[10004], d[10004];
int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    d[0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = a[i]; j <= k; j++)
            d[j] += d[j - a[i]];

    cout << d[k];
}