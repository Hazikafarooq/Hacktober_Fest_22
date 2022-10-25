#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int size;
    cout << "Size: ";
    cin >> size;
    int *myArray = new int[size];
    for (int i = 0; i < size; i++)
    {
        cout << "Array [" << i << "] ";
        cin >> myArray[i];
    }
    for (int i = 0; i < size; i++)
    {

        cout << myArray[i] << " ";
    }
    delete[] myArray;
    myArray = NULL;
    cout << myArray;
}

////////////Multidimentional arrays
//// columns ===> primary arrays    0   1    2   3
//                                  5   1    4   6
// rows address of these primary arrays ====> secondary array , 0
//                                        1
/// stack , holds the adress of secondary array, a double pointer **table

// int main()
// {
//     int row, col;
//     cout << "Rows and columns: ";
//     cin >> row >> col;
//     int **table = new int *[row];
//     for (int i = 0; i < row; i++)
//     {
//         table[i] = new int[col];
//     }
//     cout << table[1][1] << endl;
//     for (int i = 0; i < col; i++)
//     {
//         delete[] table[i];
//     }

//     delete[] table;
//     table = NULL;
// }

////////FUNCTION POINTER
// int getnum()
// {
//     return 5;
// }
// int add(int a, int b)
// {
//     return a + b;
// }
// int main()
// {
//     int a, b;
//     int (*funcptr)() = getnum; // the type returned by the func --- then name of the pointer with * , then parameter the function is recieving .
//     cout << funcptr() << endl;
//     // cin >> a >> b;
//     int (*funcptr2)(int, int) = add;
//     // cout << funcptr2(a, b);
//     cout << add(5, 5) << endl;      //one way to invoke func
//     cout << funcptr2(6, 6) << endl; // other way using pointer
// }

///ACTUAL USE OF FUNCTION POINTERS
//sorting algo in c++

bool ascending(int a, int b)
{
    return a < b;
}
bool descending(int a, int b)
{
    return a > b;
}
// void sortascending(vector<int> &vectors)  //instead of making 2 functions for sort ascen and descen we can use func pointer to create one generic func
// {
//     for (int i = 0; i < vectors.size(); i++)
//     {
//         int index = i;
//         for (int j = i + 1; j < vectors.size(); j++)
//         {
//             if (ascending(vectors[j], vectors[index]))
//             {
//                 index = j;
//             }
//         }
//         swap(vectors[i], vectors[index]);
//     }
// }

void customSort(vector<int> &vectors, bool (*funcptr)(int, int))
{
    for (int i = 0; i < vectors.size(); i++)
    {
        int index = i;
        for (int j = i + 1; j < vectors.size(); j++)
        {
            if (funcptr(vectors[j], vectors[index]))
            {
                index = j;
            }
        }
        swap(vectors[i], vectors[index]);
    }
}

void printnum(vector<int> &vectors)
{
    for (int i = 0; i < vectors.size(); i++)
    {
        cout << vectors[i] << " ";
    }
}
// int main()
// {
//     vector<int> mynum = {5, 4, 6, 2, 3, 1};
//     // sortascending(mynum);
//     // printnum(mynum);
//     //now using func pointers
//     bool (*funcptr)(int, int) = ascending;
//     customSort(mynum, funcptr);
//     printnum(mynum);
// }
