echo 'START'
cd data
for i in 32 64 96 128
do
	echo $i
	mkdir $i
	cp ../template/* $i
	cd $i
	sed -i "s/NUMBER/$i/g" INCAR.nolocal
	mv INCAR.DFT INCAR
	mv POTCAR.PBE POTCAR
	/home/j/Study/QMComp/vasp.5.4.4/vasp.5.4.4/bin/vasp_std
	mv INCAR INCAR.DFT
	mv INCAR.nolocal INCAR
	/home/j/Study/QMComp/vasp.5.4.4/vasp.5.4.4/bin/vasp_std
	cd ../
done
