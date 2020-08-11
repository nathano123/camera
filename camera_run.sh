#!/bin/bash

for i in {1..10}
do
   echo "making shot for $i time(s)"
   raspistill -o $i.jpg
   ./camera.py $i.jpg camera1 2 4
   rm $i.jpg
done
