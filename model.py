from keras.models import Model
from keras.layers import Input, Dense, Embedding, Reshape, GRU, merge, LSTM, Dropout, BatchNormalization, Activation, concatenate, multiply, MaxPooling1D, Conv1D, Flatten
from keras.optimizers import RMSprop
import keras
import tensorflow as tf

from models.attendgru import AttentionGRUModel
from models.ast_attendgru_xtra import AstAttentionGRUModel as xtra
from models.transformer import TransformerModel
from models.cmc3 import Cmc3Model as cmc3
from models.cmc4 import Cmc4Model as cmc4
from models.cmc5 import Cmc5Model as cmc5
from models.cmc7 import Cmc7Model as cmc7
from models.cmc8 import Cmc8Model as cmc8
from models.cmc9 import Cmc9Model as cmc9
from models.cmc10 import Cmc10Model as cmc10
from models.cmc11 import Cmc11Model as cmc11

def create_model(modeltype, config):
    mdl = None

    if modeltype == 'attendgru':
    	# base attention GRU model based on Nematus architecture
        mdl = AttentionGRUModel(config)
    elif modeltype == 'ast-attendgru':
    	# attention GRU model with added AST information from srcml. 
        mdl = xtra(config)
    elif modeltype == 'cmc3':
    	# sandbox model to try things
        mdl = cmc3(config)
    elif modeltype == 'cmc4':
        # sandbox model to try things
        mdl = cmc4(config)
    elif modeltype == 'cmc5':
        # sandbox model to try things
        mdl = cmc5(config)
    elif modeltype == 'cmc7':
        # sandbox model to try things
        mdl = cmc7(config)
    elif modeltype == 'cmc8':
        # sandbox model to try things
        mdl = cmc8(config)
    elif modeltype == 'cmc9':
        # sandbox model to try things
        mdl = cmc9(config)
    elif modeltype == 'cmc10':
        mdl = cmc10(config)
    elif modeltype == 'cmc11':
        mdl = cmc11(config)
    elif modeltype == 'transformer':
        # sandbox model to try things
        mdl = TransformerModel(config)
    else:
        print("{} is not a valid model type".format(modeltype))
        exit(1)
        
    return mdl.create_model()
