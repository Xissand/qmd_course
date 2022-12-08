echo 'START'
cd data
for i in `LANG=en_US seq 0.3 0.05 3.0`
do
	echo $i
	mkdir $i
	cp ../template/* $i
	cd $i
	sed -i "s/ATOM/$i/" POSCAR
	/home/j/Study/QMComp/vasp.5.4.4/vasp.5.4.4/bin/vasp_std
	cd ../
done
