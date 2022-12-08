#!/bin/bash
echo 'START'
cd data
for i in `LANG=en_US seq 0.3 0.05 3.0`
do
	echo $i
	mkdir $i
	cp ../template/* $i
	cd $i
	sed -i "s/ATOM/$i/" data.h_atom.ang
	y=$(bc -l <<< "$i/2.0")
	sed -i "s/EL/$y/" data.h_atom.ang
	lmp -in in.h_atom.spe.ang
	cd ../
done
