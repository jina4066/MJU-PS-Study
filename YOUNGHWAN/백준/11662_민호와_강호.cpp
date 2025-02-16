#include <bits/stdc++.h>
using namespace std;
int Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;
pair<double, double> minho(double p)
{
    return make_pair(Ax + (Bx - Ax) * (p / 100), (Ay + (By - Ay) * (p / 100)));
}
pair<double, double> kangho(double p)
{
    return make_pair(Cx + (Dx - Cx) * (p / 100), (Cy + (Dy - Cy) * (p / 100)));
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> Ax >> Ay >> Bx >> By >> Cx >> Cy >> Dx >> Dy;

    double l(0), h(100), minRes = 20000, p, q;
    while (h - l >= 1e-6)
    {
        p = (2 * l + h) / 3;
        q = (l + 2 * h) / 3;

        pair<double, double> m_p = minho(p);
        pair<double, double> m_q = minho(q);
        pair<double, double> k_p = kangho(p);
        pair<double, double> k_q = kangho(q);

        double ptimeD = sqrt(pow(m_p.first - k_p.first, 2) + pow(m_p.second - k_p.second, 2));
        double qtimeD = sqrt(pow(m_q.first - k_q.first, 2) + pow(m_q.second - k_q.second, 2));

        minRes = min(minRes, min(ptimeD, qtimeD));
        if (ptimeD > qtimeD)
        {
            l = p;
        }
        else
        {
            h = q;
        }
    }
    cout.precision(10);
    cout << minRes << endl;
}