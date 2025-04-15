for filenumber in {1..9};  do
	echo "tu es trop beau bebe" > "texte${filenumber}.txt"
done 

echo " Donne moi un nom pour le dossier : "
read nom

mkdir -p  ${nom}; 


for file in $(ls *.txt); do
	mv ${file} "${nom}/${file}"
done 
