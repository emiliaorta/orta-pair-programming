# Pair Programming Function

This repository contains a Python function written for the SA05-pair-programmingg assignment in GPGN268.

## Function Description

The function `offset_mean(array, target_mean)` shifts the values in an input array so that the mean of the array matches a specific target value.

The function works by:
1. Calculating the current mean of the input array.
2. Computing the difference between the current mean and the target mean.
3. Adding this offset/difference to every value in the array.

This allows the relative spacing between the values to stay the same while shifting the overall mean.

## Example

Input array:
[1, 2, 3, 4]

Current mean: 
2.5

Target mean:
10

Target mean - Current mean = 7.5

[1 + 7.5, 2 + 7.5, 3 + 7.5, 4 + 7.5]

Output:
[8.5, 9.5, 10.5, 11.5]

The new array now has a mean of 10.

