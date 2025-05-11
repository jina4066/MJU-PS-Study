#include <bits/stdc++.h>
using namespace std;
int dx[6] = {1, -1, 0, 0, 0, 0};
int dy[6] = {0, 0, 1, -1, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};
int L, R, C;
int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    while (1)
    {
        cin >> L >> R >> C;
        if (L == 0 && R == 0 && C == 0)
        {
            break;
        }
        // 3개의 원소를 가질 수 있는 tuple 자료구조 활용.
        queue<tuple<int, int, int>> Q;
        char board[32][32][32];
        int dist[32][32][32];
        bool escape = false;

        for (int x = 0; x < L; x++)
        {
            for (int y = 0; y < R; y++)
            {
                fill(dist[x][y], dist[x][y] + C, 0);
            }
        }

        for (int x = 0; x < L; x++)
        {
            for (int y = 0; y < R; y++)
            {
                for (int z = 0; z < C; z++)
                {
                    cin >> board[x][y][z];
                    // S면 BFS queue에 추가.(시작점 추가)
                    if (board[x][y][z] == 'S')
                    {
                        Q.push({x, y, z});
                        dist[x][y][z] = 0;
                    }
                    // .이면 못 가는 지역이므로 -1로 초기화
                    else if (board[x][y][z] == '.')
                    {
                        dist[x][y][z] = -1;
                    }
                }
            }
        }
        while (!Q.empty())
        {
            if (escape)
            {
                break;
            }
            auto cur = Q.front();
            Q.pop();
            int curZ, curX, curY;
            // cur의 값을 한방에 할당
            tie(curZ, curX, curY) = cur;
            for (int i = 0; i < 6; i++)
            {
                int nz = curZ + dz[i];
                int nx = curX + dx[i];
                int ny = curY + dy[i];
                if (nx < 0 || nx >= R || ny < 0 || ny >= C || nz < 0 || nz >= L)
                {
                    continue;
                }
                if (board[nz][nx][ny] == '#' || dist[nz][nx][ny] > 0)
                {
                    continue;
                }

                dist[nz][nx][ny] = dist[curZ][curX][curY] + 1;
                // 탈출 조건이면 탈출
                if (board[nz][nx][ny] == 'E')
                {
                    cout << "Escaped in " << dist[nz][nx][ny] << " minute(s).\n";
                    escape = 1;
                    break;
                }
                Q.push({nz, nx, ny});
            }
        }
        if (!escape)
        {
            cout << "Trapped!" << "\n";
        }
    }
}