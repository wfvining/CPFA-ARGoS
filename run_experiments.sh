#!/bin/bash

# for num-clusters in {1 (16x16), 4 (8x8), 16 (4x4)}
#     arena-sizes in {10, 20, 40, 80, 160},
#     detection radius in {0.05, 0.1, 0.2, 0.4, 0.8, 1.6}

if [ $# != 1 ]
then
    echo "please provide an experiment tag"
    exit
fi

tag=$1

iterations=10

let i=1
for clustersize in 4 8 16
do
    for size in 10 20 40 80 160 320
    do
        for r in 1.6 1.2 0.8 0.6 0.4 0.3 0.2 0.15 0.1
        do
            file=BCPFA_c${clustersize}_R${size}_r${r}_${tag}.argos
            erb -T - \
                csize=${clustersize} \
                sitefidelity=0.0 \
                size=${size} \
                detectionradius=${r} \
                seed=${RANDOM} \
                iterations=${iterations} \
                n=1 \
                -- experiments/BCPFAExperiment.argos.erb \
                >experiments/$file
            echo "argos3 -c experiments/$file > results/$file.results"
        done
    done
done
