#include <bits/stdc++.h>

using namespace std;
int n, m, goal_x, goal_y;
int graph[1005][1005];
bool visited[1005][1005];
int dist[1005][1005];
int x_dir[4] = {0, 1, 0, -1};
int y_dir[4] = {-1, 0, 1, 0};
void bfs(int start_y, int start_x)
{
    queue<pair<int, int>> q;
    q.push(make_pair(start_y, start_x));
    visited[start_y][start_x] = 1;
    dist[start_y][start_x]++;
    while (!q.empty())
    {
        int y = q.front().first;
        int x = q.front().second;

        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int y_new = y + y_dir[i];
            int x_new = x + x_dir[i];

            if ((0 <= x_new && x_new < m) && (0 <= y_new && y_new < n) && !visited[y_new][x_new] && graph[y_new][x_new] > 0)
            {
                visited[y_new][x_new] = 1;
                q.push(make_pair(y_new, x_new));
                dist[y_new][x_new] = dist[y][x] + 1;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] == 1 && dist[i][j] == 0)
            {
                dist[i][j] = -1;
            }
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
            if (graph[i][j] == 2)
            {
                goal_x = j;
                goal_y = i;
            }
            visited[i][j] = 0;
        }
    }
    bfs(goal_y, goal_x);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (dist[i][j] > 0)
            {
                dist[i][j]--;
            }
            cout << dist[i][j] << " ";
        }
        cout << "\n";
    }
}
// 1. 알고리즘 : 최단 거리 문제 -> 전형적인 그래프 탐색 문제이다. 이 문제의 경우 BFS를 사용했다.
// 2. 자료구조 : 각 지점은 2차원 정적배열을 사용했다.
// cf) BFS의 기본 구조만 외우고 있으면, 조건이 어렵지 않아. 쉽게 풀 수 있을거 같다.
// BFS, DFS 참고 자료 : https://jehunseo.tistory.com/225