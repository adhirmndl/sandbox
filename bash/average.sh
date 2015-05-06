#!/bin/bash
read n
sum=0
for i in `seq 1 $n`
do
    read x
    sum=$(( $sum + $x ))
done
#echo $(( $sum/$n )) 
bc -l <<< "scale=3;$sum/$n"
