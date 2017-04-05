import pandas as pd
import pickle

import os.path
dir_path = os.path.dirname(os.path.realpath(__file__))
data_set_path = dir_path + '/../dataset/'
target_jokes = dir_path+'/../target_jokes/'
csv_dataset_path = data_set_path+'csv/'
index_filename = target_jokes + 'index'
jokes_corpus = target_jokes + 'jokes_corpus'


def get_merged_csv_names():

    if not os.path.exists(index_filename):
        return None
    else:
        with open(index_filename, 'rb') as f:
            index = pickle.load(f)
            return index


def update_index(merge_list):
    with open(index_filename, 'ab') as f:
        pickle.dump(merge_list, f)


def update_jokes_corpus(new_jokes):
    with open(jokes_corpus, 'ab') as f:
        pickle.dump(new_jokes, f)


def pickle_csv_dataset(directory_name=csv_dataset_path):
    files = [each_file for each_file in os.listdir(directory_name)]
    index = get_merged_csv_names()
    if index is None:
        merge_list = files
    else:
        merge_list = [each_file for each_file in files if each_file not in index]

    if len(merge_list) > 0:
        new_jokes = []
        for each_file_name in merge_list:
            i = 0
            jokes_list = pd.read_csv(csv_dataset_path+each_file_name)
            jokes_list = pd.np.array(jokes_list)
            jokes_list = jokes_list[:,1]
            for each_joke in jokes_list:
                i += 1
                if type(each_joke) is str:
                    new_jokes.append(each_joke)
                else:
                    print('Jokes Filename: ', each_file_name)
                    print('Joke skipped: ', i)

        update_index(merge_list)
        update_jokes_corpus(new_jokes)

"""
MAIN PROGRAM STARTS HERE

The CSV folder should contain csv files of the form (Serial No, Joke)
"""
if __name__ == '__main__':
    if not os.path.exists(target_jokes):
        os.makedirs(target_jokes)
    pickle_csv_dataset()