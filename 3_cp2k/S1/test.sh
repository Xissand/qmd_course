#!/bin/bash
echo 'START'
for i in `LC_NUMERIC=en_US.UTF-8 LANG=en_US seq 0.3 0.05 3.0`
do
	echo $i
	#mkdir $i
	cp cp2k.inp.template cp2k.inp
	#cd $i
	sed -i "s/ATOMPOSITION/$i/" cp2k.inp
	~/Study/cp2k/cp2k/exe/local/cp2k.popt -i cp2k.inp -o log.$i.out
	#cd ../
done
