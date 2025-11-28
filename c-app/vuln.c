#include <stdio.h>
#include <string.h>

int main() {
    char buf[10];
    gets(buf);  // buffer overflow
    printf(buf); // format string vuln
    return 0;
}
