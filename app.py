from tkinter import *
from char_rnn.model import Model
import os.path
from six.moves import cPickle
import tensorflow as tf
from six import text_type
import string


def sample(save_dir, prime_arg):
    if not save_dir:
        save_dir = os.path.join(dir_path,'char_rnn', 'save')
    sample_freq = 1
    n=500
    prime_arg = text_type(prime_arg)
    with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, training=False)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            ret = model.sample(sess, chars, vocab, n, prime_arg,
                               sample_freq).encode('utf-8')
    ret = str(ret)
    ret = ret[1:]
    translator = str.maketrans(' ', ' ', string.punctuation[:13]+string.punctuation[14:])
    ret = ret.translate(translator)
    return ret

def show_entry_fields():
    output.insert(INSERT, sample(save_dir=save_path.get(), prime_arg=prime.get()))
    output.config(state = DISABLED)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    master = Tk()
    Label(master, text="Phrase").grid(row=0)
    Label(master, text="Save_path").grid(row=1)
    Label(master, text="Output").grid(row=2)

    prime = Entry(master)
    output = Text(master, height=10)
    save_path = Entry(master)

    prime.grid(row=0, column=1)
    save_path.grid(row=1, column=1)
    output.grid(row=2, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    mainloop()