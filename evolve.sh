#!/bin/bash
rm nohup.out
#nohup bash -c "mpirun -n $1 -machinefile $2 ~/GitHub/CPFA-ARGoS/build/cpfa_evolver -t 15 -p 50 -g 100 -c 0.1 -m 0.1 -s 1.0 -e 1 && cat evolution.txt | mail -s \"CPFA Evolution Report\" matthew@fricke.co.uk" &
nohup bash -c "~/GitHub/CPFA-ARGoS/build/cpfa_evolver -t 15 -p 50 -g 100 -c 0.1 -m 0.1 -s 1.0 -e 1 && cat evolution.txt | mail -s \"CPFA Evolution Report\" matthew@fricke.co.uk" &
