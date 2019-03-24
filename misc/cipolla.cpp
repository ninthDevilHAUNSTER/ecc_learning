#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const ll  INF = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-6;
const double pi  = acos(-1.0);

ll max(ll a, ll b) {
    return a > b ? a : b;
}

ll min(ll a, ll b) {
    return a < b ? a : b;
}

ll mul_mod(ll a, ll b, ll c) {
    ll res = 0;
    while(b) {
        if(b & 1) res = (res + a) % c;
        a = (2 * a) % c;
        b >>= 1;
    }
    return res;
}

ll pow_mod(ll a, ll b, ll c) {
    ll res = 1;
    while(b) {
        if(b & 1) res = (res * a) % c;
        a = (a * a) % c;
        b >>= 1;
    }
    return res;
}

struct T {
    ll p, d;
    T() {}
    T(ll t_p, ll t_d) : p(t_p), d(t_d) {}
};
ll w;

/* 二次域乘法 */
T multi_er(T a, T b, ll m) {
    T ans;
    ans.p = (a.p * b.p % m + a.d * b.d % m * w % m) %m;
    ans.d = (a.p * b.d % m + a.d * b.p % m) % m;
    cout << ans.p<< " "<< ans.d<<endl;
    return ans;
}

/* 二次域上快速幂 */

T power(T a, ll b, ll m) {
    T ans;
    ans.p = 1;
    ans.d = 0;
    while(b) {
        if(b & 1) {
            ans = multi_er(ans, a, m);
//            cout<< ans.p << '\t';
            b--;
        }
//        cout << endl;
        b >>= 1;
        a = multi_er(a, a, m);
    }
    return ans;
}

// 求解勒让德符号

ll legendre(ll a, ll p) {
    return pow_mod(a, (p - 1) >> 1, p);
}

ll mod(ll a, ll m) {
    a %= m;
    if(a < 0) a += m;
    return a;
}

// x^2 = n (mod p)
ll solve(ll n, ll p) {
    if(p == 2) return 1;
    if(legendre(n, p) + 1 == p) return -1;
    ll a = -1, t;
    while(true) {
        a = rand() % p;
//        cout << a << endl;
        t = a * a - n;
        w = mod(t, p);
//        cout<< w << endl;
        if(legendre(w, p) + 1 == p) break;
//        cout << w;
    }
    T tmp;
    tmp.p = a;
    tmp.d = 1;
    T ans = power(tmp, (p + 1) >> 1, p);
    return ans.p;
}

int main() {

    //freopen("aa.in", "r", stdin);
    //freopen("bb.out", "w", stdout);

    int K; ll a, p;
    scanf("%d", &K);
    while(K--) {
        cin >> a >> p;
        ll ans = solve(a, p);
        if(ans == -1) {
            cout << "No root" << endl;
            continue;
        }
        if(ans == p - ans) {
            cout << ans << endl;
        } else {
            cout << min(ans, p - ans) << " " << max(ans, p - ans) << endl;
        }
    }
    return 0;
}
