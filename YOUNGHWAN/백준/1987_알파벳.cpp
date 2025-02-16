#include <bits/stdc++.h>
using namespace std;
int n, m, a[23][23], ans;
char c;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
bool visited[30] = {
    0,
};
void dfs(int y, int x, int cnt)
{
    ans = max(ans, cnt);
    for (int i = 0; i < 4; i++)
    {
        int curY = y + dy[i];
        int curX = x + dx[i];

        if (0 <= curY && curY < n && 0 <= curX && curX < m)
        {
            if (!visited[a[curY][curX]])
            {
                visited[a[curY][curX]] = 1;
                dfs(curY, curX, cnt + 1);
                visited[a[curY][curX]] = 0;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> c;
            a[i][j] = (int)c - 'A';
        }
    }
    visited[a[0][0]] = 1;
    dfs(0, 0, 1);
    cout << ans;
}
// 백트래킹을 사용한 문제이다.
// 2차원 평면 내에서 백트래킹을 사용하기에 2차원 배열을 사용했고, 
// Char 배열보다는 Int 배열이 다루기 편해서 입력 받을 때 숫자로 치환했다.