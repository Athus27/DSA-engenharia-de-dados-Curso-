#include <iostream>
#include "interface.h"
using namespace std;

int menu() {
    int choice;


    while (true) {
        cout << "\n=== Menu ===" << endl;
        cout << "1. Option 1" << endl;
        cout << "2. Option 2" << endl;
        cout << "3. Option 3" << endl;
        cout << "4. Option 4" << endl;
        cout << "5. Option 5" << endl;
        cout << "6. Option 6" << endl;
        cout << "7. Option 7" << endl;
        cout << "8. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                cout << "You selected Option 1" << endl;
                break;
            case 2:
                cout << "You selected Option 2" << endl;
                break;
            case 3:
                cout << "You selected Option 3" << endl;
                break;
            case 4:
                cout << "You selected Option 4" << endl;
                break;
            case 5:
                cout << "You selected Option 5" << endl;
                break;
            case 6:
                cout << "You selected Option 6" << endl;
                break;
            case 7:
                cout << "You selected Option 7" << endl;
                break;
            case 8:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice. Try again." << endl;
        }
    }
}