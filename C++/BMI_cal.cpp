#include <iostream>
using namespace std;

// weight (kg)*height(m)
// underweight <18.5
// normal weight 18.5 -24.9
// overweight >25

int main()
{
    float weight, height, bmi;
    cout<<"Enter your Weight in KG: "; 		// Written to increase the readability and user interaction...
    cin >> weight;
    
    cout<<"Enter your Height in Centimeters: ";			// Written to increase the readability and user interaction...
    cin >> height;
    
    bmi = weight / ((height / 100) * (height / 100));			//Formula Correction...
    if (bmi < 18.5)
        cout << "Underweight\n";
    else if (bmi > 18.4 && bmi < 25)			// Normal BMI value range correction...
        cout << "Normal weight\n";

    else
        cout << "Overweight\n";

    cout << "your bmi is: " << bmi << endl;
}
