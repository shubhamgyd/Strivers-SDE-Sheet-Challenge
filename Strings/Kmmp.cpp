#include <iostream>
#include <vector>
#include <string>

int longProperPrefixSuffix(const std::string& str, int n) {
    for (int len = n - 1; len >= 0; len--) {
        for (int j = 0; j < len; j++){
            if (str[j] != str[n - len + j]) {
                break;
            }
        }
        if (j == len) {
            return len;
        }
    }
    return 0;
}

std::vector<int> fillLPS(const std::string& str) {
    int n = str.length();
    std::vector<int> lps(n, -1);
    lps[0] = 0;
    for (int i = 1; i < n; i++) {
        lps[i] = longProperPrefixSuffix(str, i + 1);
    }
    return lps;
}

int main() {
    std::string str = "abacabad";
    std::vector<int> lps = fillLPS(str);

    for (int val : lps) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
