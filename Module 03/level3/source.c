#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void no(){
    puts("Nope.\n");
    exit(1);
}

void ok(){
    puts("Good job.\n");
    return;
}

int main(){
    char input[24];
    char result[9];
    size_t i = 2;
    int scanf_val;
    int j = 1;
    char tmp[4];

    printf("Please enter key: ");
    scanf_val = scanf("%s", input);
    if(scanf_val != 1){
        no();
    }
    if (input[1] != '2'){
        no();
    }
    if (input[0] != '4'){
        no();
    }

    fflush(stdin);
    memset(result, 0, 9);
    result[0] = '*';
    
    while(true){
        size_t len = strlen(result);
        bool stop = false;
        if(len < 8){
            len = strlen(input);
            stop = i < len;
        }
        if(!stop)
            break;
        tmp[0] = input[i];
        tmp[1] = input[i+1];
        tmp[2] = input[i+2];
        tmp[3] = 0;
        int atoi_val = atoi(tmp);
        result[j] = (char)atoi_val;
        i += 3;
        j++;
    }
    result[j] = '\0';
    int strcmp_val = strcmp(result, "********");
    if(strcmp_val == 0){
        ok();
    }
    else{
        no();
    }
    return 0;
}