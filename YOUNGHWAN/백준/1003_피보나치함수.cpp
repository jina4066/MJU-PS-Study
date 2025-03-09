#include <bits/stdc++.h>
using namespace std;
int N, k;
int dp[41];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    while (N--)
    {
        cin >> k;
        if (k == 0)
        {
            cout << "1 0"
                 << "\n";
            continue;
        }
        else if (k == 1)
        {
            cout << "0 1"
                 << "\n";
            continue;
        }
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= k; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        cout << dp[k - 2] << " " << dp[k - 1] << "\n";
    }
    return 0;
}
// 사용 알고리즘 : DP
// 피보나치에서 0과 1의 호출 횟수를 구하는 과정이다. 잘 생각해보면 점화식을 도출할 수 있다.