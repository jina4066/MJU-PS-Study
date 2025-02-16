#include <bits/stdc++.h>
#define MAX 1004
using namespace std;
int N, M, u, v, ret;
int arr[MAX][MAX];
bool vs[MAX];
void dfs(int v)
{
    vs[v] = true;
    for (auto i = 0; i <= N; i++)
    {
        if (vs[i] == true || arr[v][i] == 0)
        {
            continue;
        }
        dfs(i);
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    while (M--)
    {
        cin >> u >> v;
        arr[u][v] = 1;
        arr[v][u] = 1;
    }
    for (auto i = 1; i <= N; i++)
    {
        if (vs[i] == false)
        {
            ret++;
            dfs(i);
        }
    }

    cout << ret << "\n";
}