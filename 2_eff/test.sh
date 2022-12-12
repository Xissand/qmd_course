#!/bin/bash
echo 'START'
cd data
for i in `LC_NUMERIC=en_US.UTF-8 LANG=en_US seq 0.3 0.05 3.0`
do
	echo $i
	mkdir $i
	cp ../template/* $i
	cd $i
	sed -i "s/ATOM/$i/" data.h_atom.ang
	x=$(python <<< "print($i*0.25)")
	y=$(python <<< "print($i*0.75)")
	sed -i "s/ELX/$x/" data.h_atom.ang
	sed -i "s/ELY/$y/" data.h_atom.ang
	lmp -in in.h_atom.spe.ang
	cd ../
done
