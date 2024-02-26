#include <stdio.h>

int main() {
    // define a variable for a integer and a pointer for an integer
    int A_var;
    int * A_ptr;
    //printf("%p\n", A_ptr);

    // Assign A the value 8
    A_var = 8;
    //printf("%p\n", A_ptr);
    // Get the memory location of A_var and assign it to A_ptr
    A_ptr = &A_var;
    // Now the pointer points to the memory (We could have done this without assigning A_var)
    //printf("%p\n", A_ptr);
    // We can 'dereference' the pointer to get to the value
    // in essence *A_ptr is the same as A_var
    printf("%d\n", *A_ptr);
    //printf("%p\n", A_ptr);
    // Q3 Here

    // End of Q3

    //printf("%p\n", A_ptr);

    // Q4 Here

    // End of Q4

    //printf("%p\n", A_ptr);
    return 0;
}