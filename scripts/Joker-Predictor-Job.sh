#!/bin/bash
#
#PBS -N "Jokes-Predictor"  
#PBS -q mamba
#PBS -l nodes=1:ppn=8,mem=64GB
#PBS -l walltime=12:00:00:00
export PYTHONPATH=$PYTHONPATH:/users/nbarnaba/.python
module load python/3.5.1
python3 /users/nbarnaba/Jokes-Predictor/word_rnn/train.py --data_dir=/users/nbarnaba/Jokes-Predictor/word_rnn/data/ --save_dir=/users/nbarnaba/Jokes-Predictor/word_rnn/save/ --log_dir=/users/nbarnaba/Jokes-Predictor/logs
