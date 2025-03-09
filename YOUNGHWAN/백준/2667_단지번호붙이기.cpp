#include <bits/stdc++.h>
using namespace std;
int arr[30][30];
bool visited[30][30];
int N, cnt, res;
string s;
vector<int> v;
// 아래, 오른쪽, 위, 왼쪽 방향 벡터 dr, dc
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

void dfs(int i, int j)
{
    for (auto l = 0; l < 4; l++)
    {
        // dfs시 방향 조정
        int a = i + dr[l];
        int b = j + dc[l];

        if (a >= N || a < 0 || b >= N || b < 0)
        {
            continue;
        }
        // 안가본 구역 + 집이 있는 구역
        if (visited[a][b] == 0 && arr[a][b] == 1)
        {
            visited[a][b] = 1;
            cnt += 1;
            dfs(a, b);
        }
    }
}
int main()
{
    // IO 최적화
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    // 입력값 받는 부분.
    for (int i = 0; i < N; i++)
    {
        cin >> s;
        for (int j = 0; j < s.length(); j++)
        {
            visited[i][j] = 0;

            if (s[j] == '1')
            {
                arr[i][j] = 1;
                continue;
            }
            arr[i][j] = 0;
        }
    }
    // 입력 행렬에서 집이 있고 안가본 곳 기준으로 DFS를 시작한다.
    for (auto i = 0; i < N; i++)
    {
        for (auto j = 0; j < N; j++)
        {
            if (arr[i][j] == 1 && visited[i][j] == 0)
            {
                visited[i][j] = 1;
                cnt = 1;
                dfs(i, j);
                v.push_back(cnt);
                res++;
            }
        }
    }
    // 오른차순 출력이라 sort
    sort(v.begin(), v.end());
    cout << res << "\n";

    for (int i : v)
    {
        cout << i << "\n";
    }
}
// 사용 알고리즘 : dfs
// matrix 형태의 입력값에서 연결 요소가 몇개로 이루어졌는지 출력하는 것이다.