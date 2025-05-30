#!/bin/bash

pip3 install ctgan sdv pandas

maindir=$(pwd)
d=$(mktemp -d)
cd $d
function cleanup {
  rm -rf "$d"
  echo "Deleted temp working directory $d"
}

trap cleanup EXIT


curl https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/KDDTrain%2B.txt > KDDTrain+.txt
curl https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/sample.py > sample.py

read -p "Enter benign percent: " pcnt

file=$(python3 sample.py $pcnt)

curl https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/train.py > train.py

python3 train.py $file $maindir $pcnt
