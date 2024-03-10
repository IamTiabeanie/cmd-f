# importing all packages
import matplotlib.pyplot as plt
#import tensorflow as tf
import numpy as np
import pandas as pd
import time 
from datetime import timedelta
import math
import os, sys
import scipy.misc
from scipy.stats import cumfreq
from random import sample
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import PIL.Image
from IPython.display import display
from glob import iglob
from io import BytesIO        

#importing data set

snakes_Train_glob = 'C:/Users/Illiyeen/Documents/GitHub/cmd-f/archive/train/**/*'
snakes_train = [f for f in iglob(snakes_Train_glob, recursive = True) if os.path.isfile(f)]
snakes_test_glob = 'C:/Users/Illiyeen/Documents/GitHub/cmd-f/archive/test/**/*'
snakes_test = [f for f in iglob(snakes_test_glob, recursive = True) if os.path.isfile(f)]

#resizing images to be smaller

image_resize = 60
def ai_training_database_creator(snakes_type, height, width, name):
    image_holder = []
    for picture in snakes_type:
        image = PIL.Image.open(snakes_type.pop())
        image = image.resize((height,width))
        image = np.array(image)
        image_holder.append(image)
    pickle.dump(image_holder, open(name + '.p', "wb"))

#final iternation of data set - next labeling

ai_training_database_creator(snakes_type = snakes_train, height = image_resize, width = image_resize, name = "train")
ai_training_database_creator(snakes_type = snakes_test, height = image_resize, width = image_resize, name = "test")
training_set = pickle.load(open("train.p", "rb"))
test_set = pickle.load(open("test.p", "rb"))

label.test = pd.read_csv("")