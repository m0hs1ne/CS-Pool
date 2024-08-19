#include <stdio.h>
#include <string.h>

int main()
{
    char read[100];
    char password[] = "__stack_check";
    printf("Please enter key: ");
    scanf("%s", read);
    int is_correct = strcmp(read, password);
    if (is_correct == 0)
        printf("Good job.\n");
    else
        printf("Nope.\n");
    return 0;
}