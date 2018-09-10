from keras.models import Model
from keras.layers import Input, Dense, Embedding, Reshape, GRU, merge, LSTM, Dropout, BatchNormalization, Activation, concatenate, multiply, MaxPooling1D, Conv1D, Flatten
from keras.optimizers import RMSprop
import keras
import tensorflow as tf

from models.attendgru import AttentionGRUModel
from models.ast_attendgru_xtra import AstAttentionGRUModel as xtra
from models.cmc1 import Cmc1Model as cmc1

def create_model(modeltype, config):
    mdl = None

    if modeltype == 'attend-gru':
    	# base attention GRU model based on Nematus architecture
        mdl = AttentionGRUModel(config)
    elif modeltype == 'ast-attendgru':
    	# attention GRU model with added AST information from srcml. 
        mdl = xtra(config)
    elif modeltype == 'cmc1':
    	# sandbox model to try things
        mdl = cmc1(config)
    else:
        print("{} is not a valid model type".format(modeltype))
        exit(1)
        
    return mdl.create_model()
