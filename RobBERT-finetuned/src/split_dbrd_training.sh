cd data/processed/dbrd

head -n 500 all.sentences.txt > eval.sentences.txt
head -n 500 all.labels.txt > eval.labels.txt

tail -n +10000 all.sentences.txt > train.sentences.txt
tail -n +10000 all.labels.txt > train.labels.txt

sed -n '501,1500p' all.sentences.txt > traintwo.sentences.txt
sed -n '501,1500p' all.labels.txt > traintwo.labels.txt