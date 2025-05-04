#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
int N;
int mat[102][102];
bool vis[102][102];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // constraints
    //  2 <= N <= 100 (integer)
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        fill(mat[i], mat[i] + N, 0);
        fill(vis[i], vis[i] + N, 0);
    }

    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < N; y++)
        {
            cin >> mat[x][y];
        }
    }
    int curMax = 0;
    for (int h = 0; h < 101; h++)
    {
        queue<pair<int, int>> Q;
        // 아래는 visit 배열 초기화
        for (int i = 0; i < N; i++)
        {
            fill(vis[i], vis[i] + N, 0);
        }
        int cnt = 0;
        // 각 원소 별로 h에 비해 원소값 비교
        for (int x = 0; x < N; x++)
        {
            for (int y = 0; y < N; y++)
            {
                if (mat[x][y] > h && !vis[x][y])
                {
                    // 높이(원소 값)가 h보다 높고, 아직 가보지 않은 지역에 대해 BFS를 진행한다.
                    Q.push({x, y});
                    vis[x][y] = 1;
                    while (!Q.empty())
                    {
                        auto cur =Q.front();
                        Q.pop();
                        for (int dir = 0; dir < 4; dir++)
                        {
                            int nx = cur.X + dx[dir];
                            int ny = cur.Y + dy[dir];

                            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                            {
                                continue;
                            }
                            if (vis[nx][ny] || mat[nx][ny] <= h)
                            {
                                continue;
                            }
                            vis[nx][ny] = 1;
                            Q.push({nx, ny});
                        }
                    }
                    cnt++;
                }
            }
        }
        curMax = max(cnt, curMax);
    }
    cout << curMax;
}