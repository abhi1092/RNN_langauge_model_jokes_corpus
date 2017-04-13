# Jokes Predictor
[![Build Status](https://travis-ci.org/naveendennis/Jokes-Predictor.svg?branch=master)](https://travis-ci.org/naveendennis/Jokes-Predictor)

## Objective

To build a jokes predictor which when trained on a dataset predicts the end of a joke. The goal is to make the system skillful enough to come up with their own jokes

## Setup

The following setups should be performed before running the training.
 1. Run the `pickle-dataset.py` to prepare the jokes for training - It creates the input.txt file in the target_jokes folder
 2. Run the `train.py` with option `--data_dir=./target_jokes` - So, that the input.txt file is linked to the RNN for training
