cd data
for i in 150 200 250 300 350
do
	echo $i
	cp ../template/extract.sh $i
	cd $i
    ./extract.sh
    cd ..
done
