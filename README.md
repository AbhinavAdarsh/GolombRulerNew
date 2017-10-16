# GolombRulerNew
Optimal Golomb Ruler Implementation

A Golomb ruler is a set of marks at integer positions along an imaginary ruler such that no two pairs of marks
are the same distance apart. The number of marks on the ruler is its order, and the largest distance between 
two of its marks is its length. Translation and reflection of a Golomb ruler are considered trivial, so the 
smallest mark is customarily put at 0 and the next mark at the smaller of its two possible values.

A Golomb ruler is optimal if no shorter Golomb ruler of the same order exists. Creating Golomb rulers is easy,
but finding the optimal Golomb ruler (or rulers) for a specified order is computationally very challenging.
Our project contains implementation only for finding Optimal ruler.

Reference : https://en.wikipedia.org/wiki/Golomb_ruler
