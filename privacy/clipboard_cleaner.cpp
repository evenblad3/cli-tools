#include <windows.h>
//#include <iostream>

bool clipboard() {
    if (!OpenClipboard(NULL)) {
        //std::cerr << "Failed to open clipboard!\n";
        return false;
    }

    struct clipboardDistructor {
        ~clipboardDistructor() {
            CloseClipboard();
        }
    } cd;

    if (!EmptyClipboard()) {
        //std::cerr << "Failed to empty clipboard!\n";
        return false;
    } else {
        //std::cout << "Clipboard contents cleared!\n";
        return true;
    }

    return true;
}

int main() {
    const int second = 1000;
    while (1) {
        clipboard();
        Sleep(second * 20);
    }
    return 0;
}
