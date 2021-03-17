#include <stdio.h>
#include <stdbool.h>

/* shift the bits the left the by the value of bits plus one then perform a
 * binary's one complement operator on it
*/
unsigned long get_max_decimal(int bits)
{
    // Get the binary length
    unsigned long binary = 1L << bits;
    // Subtract one to be able to or them
    unsigned long or_value = binary - 1;
    // Or the values
    binary = binary | or_value;
    // Drop a bit and that should get you the right result
    binary = binary >> 1;

    return binary;
}

void print_range(int bytes, bool is_signed)
{
    // calculate the number of its the data type has
    int bits = bytes * 8;
    if (is_signed)
    {
        unsigned long max_decimal;
        long min_decimal;
        max_decimal = get_max_decimal(bits - 1);
        min_decimal = (get_max_decimal(bits - 1) + 1) * -1;
        printf("The range of %i byte is: %ld - %lu\n", (bits / 8), min_decimal, max_decimal);
    }

}
int main(void)
{
    char signed_char;
    short signed_short;
    int signed_int;
    long signed_long;


    print_range(sizeof(signed_char), true);
    print_range(sizeof(signed_short), true);
    print_range(sizeof(signed_int), true);
    print_range(sizeof(signed_long), true);

    return 0;
}
