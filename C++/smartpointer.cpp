#include <iostream>
#include <memory>
using namespace std;

///// UNIQUE POINTERS, SHARED POINTERS, Weak Pointers

// int main()
// {
//     unique_ptr<int> unPtr1 = make_unique<int>(25);
//     cout << *unPtr1 << endl;
//     //it can't share for ex unique_ptr<int>unPtr2=unPtr1;
//     //instead
//     unique_ptr<int> unptr2 = move(unPtr1);
//     cout << *unptr2 << endl;
// }

///lets see an example of unique pointers using class constructors and destructors
class myClass
{
public:
    myClass()
    {
        cout << "Constructors invoked! \n";
    }
    ~myClass()
    {
        cout << "destructors invoked! \n";
    }
};
int main()
{

    unique_ptr<myClass> unptr = make_unique<myClass>();
    // shared pointers
    shared_ptr<myClass> shptr1 = make_shared<myClass>();
    cout << "Shared count: " << shptr1.use_count() << endl;
    {
        shared_ptr<myClass> shptr2 = shptr1;
        cout << "Shared count: " << shptr1.use_count() << endl;
    }
    cout << "Shared count: " << shptr1.use_count() << endl;
    ////weak pointer
    // weak_ptr<int> weptr1;
    // {
    //     shared_ptr<int> shptr1 = make_shared<int>(25);
    //     weptr1 = shptr1;
    //     cout << *weptr1 << endl;
    // }
}
