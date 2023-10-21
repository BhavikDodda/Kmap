# Kmap

Minimizes any N-variable function given the minterms

## Algorithm

### Standard process for 4 variable functions

- We first see if it contains all of the minterms. If so, the minimized function will just be f(a,b,c,d)=1
- If the first condition fails, we move down to finding all the octets and notice what variables remain constant among the minterms of each of the octets. We consider this in the minimized function.
- If all the elements are not exhausted, we move down again to finding all the quads and repeat this process again for pairs and single minterms that are left out.

  The process halts once all the minterms are covered in atleast one "tet"

- Number of octets= 8
- Number of quads= 24
- Number of pairs= 32


### Generalized algorithm

Let's call octets as 3-tets, quads as 2-tets and pairs as 1-tets etc.

An n-tet will contain 2^n elements/minterms.

Given an N variable function $f(x_1,x_2,...x_N)$ as a sum of minterms, to minimize it we'll have to go through N-tets first, (N-1)tets, (N-2) tets and so on uptill 0-tets in decreasing order.

- A pair or a 1-tet in an N variable function will have 2^1 minterms whose N-1 variables in the product within each term are the same across all the minterms in the set and 1 variable that's varying.
  - Example: (0,1,0,0,1,1,0),(0,0,0,0,1,1,0) is a pair where 6 out of the 7 parts are constant and 1 part (in index 1) is varying
  - Number of pairs = number of ways to choose 1 varying variable * the left out constant variable combinations for chosen varying variables = $^N C _1 \cdot 2^{N-1}$
- A quad or a 2-tet in an N variable function will have 2^2 minterms whose N-2 variables in the product within each term are the same across all the minterms in the set and 2 variables that are varying.
  - Example: (0,1,0,0,1,1,0),(0,0,0,0,1,1,0),(0,1,0,0,0,1,0),(0,0,0,0,0,1,0) is a quad where 5 out of the 7 parts are constant and 2 parts (indices 1,4) are varying
  - Number of quads = number of ways to choose 2 varying variables * the left out constant variable combinations for chosen varying variables = $^N C _2 \cdot 2^{N-2}$
- An octet or a 3-tet in an N variable function will have 2^3 minterms whose N-3 variables in the product within each term are the same across all the minterms in the set and 3 variables that are varying.
  - Example: (0,1,0,0,1,1,0),(0,0,0,0,1,1,0),(0,1,0,0,1,1,0),(0,0,0,0,0,1,0),(0,1,0,0,1,1,1),(0,0,0,0,1,1,1),(0,1,0,0,1,1,1),(0,0,0,0,0,1,1) is an octet where 4 out of 7 parts are constant and 3 parts (indices 1,4,6) are varying.
  - Number of octets = number of ways to choose 3 varying variable * the left out constant variable combinations for chosen varying variables = $^N C _3 \cdot 2^{N-3}$

So, the number of possible n-tets in an N variable function would be: $^N C _n \cdot 2^{N-n}$

As k varies from 0 to N, we generate all possible (N-k) tets and see if the function contains all the minterms of the tets. If they do, then a minimized term is added for every such tet. We let this process run until every possible minterm is included in one of the tets.

- Worst case scenario: It halts when k=N. Occurs when a minterm itself has to be included in the minimized expression where the minterm doesn't have any adjacent minterms present in the function and no n-tet for n>1 can include the term.
- Best case scenario: It halts when k=0. Occurs when the given function is a complete DNF, and the minimized function is (1)