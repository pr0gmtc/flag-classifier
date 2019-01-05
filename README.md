# Flag Classifier
A small project in which I used [scikit decision tree model](https://scikit-learn.org/stable/modules/tree.html) to create script that can classify flags by different parameters such as colors, number of vertical bars, number of horizontal stripes, etc.

# Dataset
I used [this](https://archive.ics.uci.edu/ml/datasets/Flags) dataset to train prediction model.

After deleting unnecessary and labeling remaining columns it looked something like this:


| name | bars | stripes | colours | red | green | blue | gold |	white	| black |	orange	| circles |	crosses	| saltires |	quarters	| sunstars |	crescent |	triangle |	icon |	animate	| text |
| ---- | ---- | ------- | ------- | --- | ----- | ---- | ---- | ----- | ----- | ------- | ------- | ------- | -------- | ---------- | -------- |  -------- | --------- | ----- | -------- | ---- | 
Afghanistan	| 0 |	3 |	5 |	1 |	1 |	0 |	1 |	1 |	1 |	0 |	0 | 0 |	0 |	0 |	1 |	0 |	0 |	1 |	0 |	0 |
Albania	| 0 |	0 |	3 |	1 |	0 |	0 |	1 |	0 | 1 |	0 |	0 |	0 |	0 |	0 |	1 |	0 |	0 |	0 |	1 |	0 |
Algeria	| 2 |	0 |	3 |	1 |	1 |	0 |	0 |	1 |	0 |	0 |	0 |	0 |	0 |	0 |	1 |	1 |	0 |	0 |	0 |	0 |
...
Zimbabwe | 0 | 7 | 5 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |

>Attribute Information:
>
>1. name:	Name of the country concerned 
>8. bars: Number of vertical bars in the flag 
>9. stripes: Number of horizontal stripes in the flag 
>10. colours: Number of different colours in the flag 
>11. red: 0 if red absent, 1 if red present in the flag 
>12. green: same for green 
>13. blue: same for blue 
>14. gold: same for gold (also yellow) 
>15. white: same for white 
>16. black: same for black 
>17. orange: same for orange (also brown) 
>19. circles: Number of circles in the flag 
>20. crosses: Number of (upright) crosses 
>21. saltires: Number of diagonal crosses 
>22. quarters: Number of quartered sections 
>23. sunstars: Number of sun or star symbols 
>24. crescent: 1 if a crescent moon symbol present, else 0 
>25. triangle: 1 if any triangles present, 0 otherwise 
>26. icon: 1 if an inanimate image present (e.g., a boat), otherwise 0 
>27. animate: 1 if an animate image (e.g., an eagle, a tree, a human hand) present, 0 otherwise 
>28. text: 1 if any letters or writing on the flag (e.g., a motto or slogan), 0 otherwise 

# Usage

flag-classifier can guess which flag has given attributes(you can just press enter instead of entering 0).
![Entering flag's and parameters and getting "South Korea" result](../master/Screenshot%20from%202019-01-05%2018-23-01.png)
