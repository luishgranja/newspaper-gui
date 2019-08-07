%Lectura de datos:
int: n; %número de temas
array[1..n] of int: inter; %personas interesadas en el tema i
array[1..n,1..2] of int: num_paginas; %núm páginas min-max para el tema i
int: NP; %máximo número de páginas

%Variables:
array[1..n] of var bool: elegido; %si el tema i va o no
array[1..n] of var int: np_tema; %núm.páginas del tema i

%Restricciones:
constraint sum(j in 1..n)(np_tema[j]* elegido[j]) <= NP;
constraint forall(i in 1..n)(num_paginas[i,1] <= np_tema[i] /\ np_tema[i] <= num_paginas[i,2]);

%Objetivo
var int: lectores;
constraint lectores = sum(j in 1..n)(np_tema[j]* elegido[j]* inter[j]);
solve maximize lectores;


 