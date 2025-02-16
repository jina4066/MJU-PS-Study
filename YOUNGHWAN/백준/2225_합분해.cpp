#include <bits/stdc++.h>
#define moduler 1000000000
#define MAX 210
int K, N;
long long dp[MAX][MAX];
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;

    for (int i = 0; i <= N; i++)
    {
        dp[1][i] = 1;
    }

    for (int k = 2; k <= K; k++)
    {
        for (int n = 0; n <= N; n++)
        {
            for (int i = 0; i <= n; i++)
            {
                dp[k][n] = dp[k][n] + dp[k - 1][i];
            }
            dp[k][n] = dp[k][n] % moduler;
        }
    }

    cout << dp[K][N] << "\n";
}
// DP를 사용하여 불었다.
// k의 의미는 k개의 수의 합을 의미한다.
// 각 루프의 자세한 이야기는 PR에 적어 놓겠음.
// moduler는 출력할 때 10억으로 나눈 나머지를 출력하라 해서 했다. 아마 큰 수의 처리 때문일거 같다.