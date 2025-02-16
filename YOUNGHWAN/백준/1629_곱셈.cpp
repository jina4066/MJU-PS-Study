#include <bits/stdc++.h>
using namespace std;
int a, b, c, res;

long long d;
long long f(long long int y)
{
    if (y == 0 || y == 1)
        return a % c;
    long long k = f(y / 2) % c;
    if (y % 2 == 0)
        return k * k % c;
    else
        return k * k % c * a % c;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a >> b >> c;
    res = f(b);
    cout << res;
    return 0;
}