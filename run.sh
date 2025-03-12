#!/bin/bash

pip install ctgan sdv

maindir=$(pwd)
d=$(mktemp -d)
cd $d
function cleanup {
  rm -rf "$d"
  echo "Deleted temp working directory $d"
}

trap cleanup EXIT


wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/KDDTrain%2B.txt
wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/sampler.py

read -p "Enter benign percent: " pcnt

file=$(python3 sampler.py pcnt)

echo "file"
#wget https://raw.githubusercontent.com/curtisjbradley/429Project/refs/heads/main/train.py
