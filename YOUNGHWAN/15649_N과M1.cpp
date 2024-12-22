#include <bits/stdc++.h>
using namespace std;
int N, M;
int sequence[10] = {
    0,
};
bool visited[10];
void dfs(int depth)
{
    if (depth == M)
    {
        for (int i = 0; i < depth; i++)
        {
            cout << sequence[i] << ' ';
        }
        cout << "\n";
        return;
    }
    for (int i = 1; i <= N; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            sequence[depth] = i;
            dfs(depth + 1);
            visited[i] = 0;
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    dfs(0);
}
// 1. 알고리즘 : 백트래킹, 문제를 보시면 알다시피, 조합을 찾는 문제. 조합 구현시 백트래킹 사용하기에 선택.