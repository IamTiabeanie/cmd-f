# importing all packages
import matplotlib.pyplot as plt
#import tensorflow as tf
import numpy as np
import pandas as pd
import time 
from datetime import timedelta
import math
import os
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

