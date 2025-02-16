#include <bits/stdc++.h>
using namespace std;
int a;
string s, pre, pro, t;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> a;
    cin >> s;

    int pos = s.find('*');
    pre = s.substr(0, pos);
    pro = s.substr(pos + 1);

    for (int i = 0; i < a; i++)
    {
        cin >> t;
        if (pre.size() + pro.size() <= t.size())
        {
            if (pre == t.substr(0, pre.size()) && pro == t.substr(t.size() - pro.size()))
            {
                cout << "DA\n";
            }
            else
            {
                cout << "NE\n";
            }
        }
        else
        {
            cout << "NE\n";
        }
    }
    return 0;
}