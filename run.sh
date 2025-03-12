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


wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/KDDTrain%2B.txt
wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/sample.py

read -p "Enter benign percent: " pcnt

file=$(python3 sample.py $pcnt)

wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/train.py

python3 train.py $file $maindir
