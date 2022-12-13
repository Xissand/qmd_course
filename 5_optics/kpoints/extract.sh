cd data
for i in 4 6 8 10 12 14 16
do
	echo $i
	cp ../template/extract.sh $i
	cd $i
    ./extract.sh
    cd ..
done