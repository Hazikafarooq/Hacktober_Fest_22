#include <iostream>
using namespace std;

// weight (kg)*height(m)
// underweight <18.5
// normal weight 18.5 -24.9
// overweight >25

int main()
{
    float weight, height, bmi;

    cin >> weight >> height;
    bmi = weight / (height * height);
    if (bmi < 18.5)
        cout << "Underweight\n";
    else if (bmi > 18.5 && bmi < 24.9)
        cout << "Normal weight\n";

    else
        cout << "Overweight\n";

    cout << "your bmi is: " << bmi << endl;
}
