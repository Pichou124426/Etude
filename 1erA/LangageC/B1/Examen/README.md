# Examen 1SYSD Clermont-Ferrant 17 décembre 2024

Sont attendus : un répertoire `Examen` à la base de votre dépôt GIT. Ce dépôt contenant :

- Un fichier `Makefile` permettant de constuire tous les binaires exécutables des fichiers
sources que vous fournissez avec la simple commande `make`, sans erreur et sans _warnings_.

- Les fichiers sources C des questions auquelles vous avez répondu.

Commandes GNU/Linux pour préparer la suite :

~~~~
$ cd ~/1sysdCF24
$ pwd
/home/.../1sysdCF24
$ git pull
$ ls
...
$ cd ~/1sysd
$ pwd
/home/.../1sysd
$ mkdir Examen
$ cd Examen
$ pwd
/home/.../1sysd/Examen
$ cp ~/1sysdCF24/* .
$ ls
Makefile + README.md + fichiers .c
~~~~

**En cas de doute ou d'échec de ces commandes n'hésitez pas à m'appeler.**

Par la suite vous aurez à adapter le fichier `Makefile` en ajoutant les noms des
programmes à la suite de la ligne `PROGS=...`

## Partie 1 : `multtab.c` et `multtab2.c`

1. Source : `multtab.c` construit à partir du modèle du même nom fournit ici.

La fonction d'affichage d'un tableau d'entier est fournie.

Compléter le code avec la définition d'une fonction de prototype `void multtab(int t1[], int t2[], int size, int result[])`
qui multiplie terme à terme les deux tableaux de nombres entiers passées en arguments à la fonction, ainsi
que leurs tailles supposées identiques, le résultat étant stocké dans le tableau `result`.

Le modèle contient déjà le code de test. Ne modifiez pas le corps de la fonction `main`.

~~~~
$ ./multtab
tab1 :2 3 42 12 9 0 
tab2 :6 7 9 10 11 88 
multtab(tab1, tab2, 6, ...) : 12 21 378 120 99 0 
~~~~

2. Source : `multtab2.c` (modèle fourni) :
en reprenant le code de votre fonction précédente `multtab` qui sera maintenant
de prototype `void multtab(int t1[], int t2[], int size1, int size2, int result[])` et qui multiplie toujours
terme à terme les éléments de _t1_ et _t2_ et s'arrête dès que la fin d'un des deux tableaux _t1_ ou _t2_
est atteinte. Le modèle `multtab2.c` fourni contient le code de test.

~~~~
$ ./multtab2
tab1 :2 3 42 12 9 0 
tab2 :6 7 9 10 11 88 
multtab(tab1, tab2, 6, 6, ...) : 12 21 378 120 99 0 
tab3 :6 8 10 
multtab(tab1, tab3, 6, 3, ...)  : 12 24 420 
multtab(tab3, tab2, 6, 3, ...)  : 36 56 90 
~~~~

## Partie 2 : `ndigits.c`

Créez un fichier `ndigits.c` en y définissant la fonction `int n_digits(char *s)` qui renvoie le nombre
de chiffres (caractères '0', '1', '2', ... '9') présents dans une chaîne _s_. Dans le corps du programme
(fontion `main`) vérifiez que le programme a bien reçu un et un seul argument en ligne de commande et
affiche un message sinon puis s'interrompt. Si un argument a été reçu il affiche le nombre de chiffres
contenus dans celui-ci.

Voici comment doit se comporter votre programme :

~~~~
$ ./ndigits
Usage: ./ndigits text
$ ./ndigits clermont123901ferrant678
9
$ ./ndigits versailles
0
$ ./ndigits 0123456789
10
~~~~

## Partie 3 : `histogram.c`

Note : il n'est pas nécessaire d'utiliser de tableaux supplémentaires dans cet exercice, pour aucun des deux
programmes.

Compléter le code de la fonction `display_histogram(int tab[], int size)` afin d'afficher un histogramme horizontal à partir des valeurs de tests :

~~~~
$ ./histogram
****
*********
********
**

*
**********
*****
********
~~~~

**Bonus** (2 pts à gagner en plus de la note sur 20 pour cette partie !)

Écrivez un programme `histogram_vert.c` pour obtenir un résultat tel que (histograme vertical)

~~~~
$ ./histogram_vert
10|                   *
 9|    *              *
 8|    *  *           *     * 
 7|    *  *           *     * 
 6|    *  *           *     * 
 5|    *  *           *  *  * 
 4| *  *  *           *  *  * 
 3| *  *  *           *  *  * 
 2| *  *  *  *        *  *  * 
 1| *  *  *  *     *  *  *  * 
 0| 4  9  8  2  0  1 10  5  8 
~~~~

## Partie 4 : `courses.c`

Compléter le code fourni dans `course.c` (fonction `void mescourses(prod tab[], int size)` pour afficher le contenu d'un panier de courses ainsi que son coût total.

Votre programme doit se comporter ainsi (avec le tableau de test fourni dans `main`) :

~~~~
$ ./courses
----------------
  Mes courses
----------------
Pommes
  Prix   : 2.23
  Nombre : 4
  Total  : 8.92
Poires
  Prix   : 3.10
  Nombre : 5
  Total  : 15.50
Cerises  :
  Prix   : 6.15
  Nombre : 10
  Total  : 61.50
----------------
TOTAL    : 85.92
~~~~

## Partie 5 : `intlist.c`

1. Introduire dans le source `intlist.c` une fonction supplémentaire `void double(node *head)` qui multiplie
par 2 tous les éléments d'une liste chaînée.

2. Introduire dans le source `intlist.c` une fonction supplémentaire `node *removelast(note *head)`
qui supprime le dernier élément d'une liste si elle a au moins un élément et la laisse inchangé sinon.
_(le code de test est fournit dans les commentaires à la fin de la fonction `main`, il vous suffit
de supprimer les `//` en début de ligne pour tester votre fonction).


