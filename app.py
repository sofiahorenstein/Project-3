from flask import (Flask,render_template,jsonify)
from joblib import load
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
