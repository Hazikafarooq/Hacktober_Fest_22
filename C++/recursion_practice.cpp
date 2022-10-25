#include <iostream>
using namespace std;

//sum from m to n first usnig loops
// int main()
// {
//     int m = 2, n = 6;
//     int sum=0;
//     for (int i = m; m <= n; m++)
//     {
//         sum += i;
//     }
//     cout << "sum: " << sum << endl;
// }

//now recursion
// int recursive_sum(int m, int n)
// {
//     if (m == n)
//         return m;
//     else
//         return m + recursive_sum(m + 1, n);
// }
// int main()
// {
//     int m = 2, n = 4;
//     cout << recursive_sum(m, n);
// }

int factorial(int n)
{
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}
int main()
{
    int n = 4;
    cout << factorial(n);
}
