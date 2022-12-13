cd data
for i in 32 64 96 128
do
	echo $i
	cp ../template/extract.sh $i
	cd $i
    ./extract.sh
    cd ..
done