#include <bits/stdc++.h>
using namespace std;
int n, x, a[250005];
long long psum[250005];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> x;
    psum[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        psum[i] = psum[i - 1] + a[i];
    }
    long long curMax = psum[x] - psum[0];
    int cnt = 1;
    for (int i = 1 + x; i <= n; i++)
    {
        long long curPsum = psum[i] - psum[i - x];
        if (curMax == curPsum)
        {
            ++cnt;
        }
        if (curMax < curPsum)
        {
            curMax = curPsum;
            cnt = 1;
        }
    }
    if (curMax == 0)
    {
        cout << "SAD";
        return 0;
    }
    cout << curMax << "\n"
         << cnt;
}
// 1. 알고리즘 : Prefix Sum 문제이다. sliding window와 함께 사용했다.
// 2. 문제 풀이 : Psum(누적합) 배열을 생성, 값을 저장한다. 그 다음에 sliding window 사용해서 curMax의
// 최대를 구하고, 만일 그 최대랑 같은 값이 등장한다면 cnt를 올리는 식으로 해결했다. 
// curMax가 0과 같으면 문제 조건에 맞게 SAD 출력하게 했다.