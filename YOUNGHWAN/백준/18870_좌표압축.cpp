#include <bits/stdc++.h>
using namespace std;
int n, e;
vector<int> v;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> e;
        v.push_back(e);
    }
    vector<int> res(v);

    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());

    for (auto i : v)
    {
        auto e = lower_bound(res.begin(), res.end(), i);
        cout << distance(res.begin(), e) << " ";
    }
}
// 좌표의 크기를 정렬했을 때 몇번째 위치인지 나타내는 문제이다.
// 난 배열을 두개 사용해서 풀었다. (하나는 원배열, 하나는 중복제거 정렬용 배열)
// 2번째 배열로 find()함수를 사용하여 몇번째 요소인지 알아내려 했지만, 시간 초과가 떠 인터넷을 뒤졌다.
// lower_bound()라는 이진탐색으로 찾는 메소드를 발견해서 사용했더니 시간초과가 안났다.
// 아마 해쉬 맵 등의 log(n) 자료구조를 잘 사용하면 선형 배열이 아니여도 풀릴 수 있을거 같다.