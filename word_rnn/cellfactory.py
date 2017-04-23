from tensorflow.contrib import rnn


class CellFactory:
    @staticmethod
    def get_cell_instance(instance_type='lstm'):
        if instance_type == 'rnn':
            cell_fn = rnn.BasicRNNCell
        elif instance_type == 'gru':
            cell_fn = rnn.GRUCell
        elif instance_type == 'lstm':
            cell_fn = rnn.BasicLSTMCell
        elif instance_type == 'nas':
            cell_fn = rnn.NASCell
        else:
            raise Exception("model type not supported: {}".format(instance_type))
