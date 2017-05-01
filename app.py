from tkinter import *
import char_rnn.model as cm
import word_rnn.model as wm
import os.path
from six.moves import cPickle
import tensorflow as tf
from six import text_type
import string


def get_char_rnn_sample(save_dir, prime_arg, n, sample_freq):
    if not save_dir:
        save_dir = os.path.join(dir_path,'char_rnn', 'save')
    if not n:
        n = 500
    else:
        n = int(str(n))
    prime_arg = text_type(prime_arg)
    with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    my_model = cm.Model(saved_args, training=False)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            ret = my_model.sample(sess, chars, vocab, n, prime_arg,
                               sample_freq).encode('utf-8')
    ret = str(ret)
    ret = ret[1:]
    translator = str.maketrans(' ', ' ', string.punctuation[:13]+string.punctuation[14:])
    ret = ret.translate(translator)
    return ret[: 1+ret.rfind('.')]


def get_word_rnn(prime_arg, n, sample_freq, pick=1, width=4):
    if not n:
        n = 500
    else:
        n = int(str(n))
    save_dir = os.path.join(dir_path,'word_rnn', 'save')
    with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(save_dir, 'words_vocab.pkl'), 'rb') as f:
        words, vocab = cPickle.load(f)
    my_model = wm.Model(saved_args, True)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            ret = my_model.sample(sess, words, vocab, n, prime_arg, sample_freq, pick, width)
    ret = str(ret)
    ret = ret[1:]
    translator = str.maketrans(' ', ' ', string.punctuation[:13] + string.punctuation[14:])
    ret = ret.translate(translator)
    return ret[: 1 + ret.rfind('.')]


def show_entry_fields():
    if model_type.get() == 'char_rnn':
        output.insert(INSERT, get_char_rnn_sample(save_dir=chosen_dataset.get(),
                                                  prime_arg=prime.get(),
                                                  n=number_of_characters.get(),
                                                  sample_freq=temperature.get()))
    else:
        output.insert(INSERT, get_word_rnn(prime_arg=prime.get(),
                                           n=number_of_characters.get(),
                                           sample_freq=temperature.get()))
    output.config(state = DISABLED)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    master = Tk()
    master.title('Jokes Generator')
    locations = dict()
    locations['default'] = os.path.join(dir_path, 'char_rnn', 'save')
    locations['l1'] = os.path.join(dir_path,'char_rnn', 'l1', 'save')
    locations['l2'] = os.path.join(dir_path,'char_rnn', 'l2', 'save')
    locations['l3'] = os.path.join(dir_path,'char_rnn', 'l3', 'save')
    locations['l4'] = os.path.join(dir_path,'char_rnn', 'l4', 'save')
    locations['l5'] = os.path.join(dir_path,'char_rnn', 'l5', 'save')

    """
        The labels are placed below
    """

    Label(master, text="Phrase").grid(row=1)
    Label(master, text="Temperature").grid(row=2)
    Label(master, text="Sampled Word Count").grid(row=3)
    Label(master, text="Model Type").grid(row=4)
    Label(master, text="Datasets").grid(row=5)
    Label(master, text="Output").grid(row=6)

    """
        The control components are placed below
    """

    prime = Entry(master)
    output = Text(master, height=10)
    model_type = StringVar(master)
    model_type.set('char_rnn')
    types = OptionMenu(master, model_type, 'char_rnn', 'word_rnn')
    chosen_dataset = StringVar(master)
    chosen_dataset.set(locations['default'])
    data_types = OptionMenu(master,
                            chosen_dataset,
                            locations['default'],
                            locations['l1'],
                            locations['l2'],
                            locations['l3'],
                            locations['l4'],
                            locations['l5'])
    number_of_characters = Entry(master)
    temperature = IntVar(master)
    temperature.set(1)  # default value
    temperature_options = OptionMenu(master, temperature, 0, 1, 2)

    prime.grid(row=1, column=1)
    number_of_characters.grid(row=3, column=1)
    temperature_options.grid(row=2, column=1)
    types.grid(row=4, column=1)
    data_types.grid(row=5, column=1)
    output.grid(row=6, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=show_entry_fields).grid(row=7, column=1, sticky=W, pady=4)
    mainloop()
