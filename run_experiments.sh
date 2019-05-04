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
mkdir experiments_${tag}

iterations=100

let i=1
for n in 1 10 100
do
    for clustersize in 8 16 32 64 128
    do
        for size in 100
        do
            for r in 0.2
            do
                file=GCPFA_c${clustersize}_R${size}_n${n}_r${r}_${tag}.argos
                erb -T - \
                    csize=${clustersize} \
                    sitefidelity=100.0 \
                    size=${size} \
                    detectionradius=${r} \
                    seed=${RANDOM} \
                    iterations=${iterations} \
                    n=${n} \
                    -- experiments/BCPFAExperiment.argos.erb \
                    >experiments_${tag}/$file
                echo "cd ~/research/CPFA-ARGoS; argos3 -c experiments_${tag}/$file > results_${tag}/$file.results; cd ../.."
            done
        done
    done
done
