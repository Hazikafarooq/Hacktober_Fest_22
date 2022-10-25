#include <iostream>
using namespace std;

char *stutter(char *msg, int n)
{
    int len = 0;
    for (int i = 0; msg[i]; i++)
        len++;

    char *res = new char[len * n + 1];

    int j = 0;
    for (int i = 0; msg[i]; i++)
    {
        for (int k = 0; k < n; k++)
        {
            res[j++] = msg[i];
        }
    }
    return res;
}

int main()
{
    int n1, n;

    cin >> n;
    cin >> n1;
    char *arr = new char[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    char *res;
    res = stutter(arr, n1);
    for (int i = 0; i < n; i++)
    {
        cout << res[i] << " ";
    }
}
