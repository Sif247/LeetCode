#include <stdlib.h>
#include <stdbool.h>

int* plusOne(int* digits, int digitsSize, int* returnSize)
{
    bool newElement = false;
    digits[digitsSize - 1]++;

    for (int i = digitsSize - 1; i >= 0; i--)
    {
        if (digits[i] == 10)
        {
            digits[i] = 0;
            if (i == 0)
            {
                newElement = true;
            }
            else
            {
                digits[i - 1]++;
            }
        }
    }

    int* ris;
    *returnSize = digitsSize;
    if (newElement == true)
    {
        ris = (int*)calloc(digitsSize + 1, sizeof(int));
        ris[0] = 1;
        (*returnSize)++;
        for (int x = 1; x < *returnSize; x++)
        {
            ris[x] = digits[x - 1];
        }
    }
    else
    {
        ris = (int*)calloc(digitsSize, sizeof(int));
        for (int x = 0; x < *returnSize; x++)
        {
            ris[x] = digits[x];
        }
    }
    
    
    return ris;
}

int main()
{
    int digits1[] = { 1,2,3 };
    int digitsSize1 = 3;
    int returnSize1 = 0;
    int* ris1 = plusOne(digits1, digitsSize1, &returnSize1);

    int digits2[] = { 4,3,2,1 };
    int digitsSize2 = 4;
    int returnSize2 = 0;
    int* ris2 = plusOne(digits2, digitsSize2, &returnSize2);

    int digits3[] = { 9 };
    int digitsSize3 = 1;
    int returnSize3 = 0;
    int* ris3 = plusOne(digits3, digitsSize3, &returnSize3);

    free(ris1);
    free(ris2);
    free(ris3);
    return 0;

}