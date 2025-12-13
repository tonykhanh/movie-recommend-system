from datetime import datetime
from distutils.command.upload import upload
from django.db import models
import datetime
import os
import pickle
import pandas as pd
import sys

# Create your models here.
# Fix for pandas compatibility with older pickle files
# Map deprecated pandas classes to new ones for pickle compatibility
pd.Int64Index = pd.Index
pd.Float64Index = pd.Index
pd.UInt64Index = pd.Index
try:
    import pandas.core.indexes.numeric as numeric_index
except ModuleNotFoundError:
    import pandas as numeric_index
    sys.modules['pandas.core.indexes.numeric'] = numeric_index

# Also add to _libs for compatibility
if hasattr(pd, '_libs'):
    pd._libs.Int64Index = pd.Index
    pd._libs.Float64Index = pd.Index
    pd._libs.UInt64Index = pd.Index
    
with open('./model/movie_list.pkl', 'rb') as m:
    movies = pickle.load(m)
with open('./model/similarity.pkl', 'rb') as s:
    similarity = pickle.load(s)


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('./static/assets/images/movies/', filename)

class Movie(models.Model):
    img = models.ImageField(upload_to = filepath, null = True, blank = True)
    rate = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    cate = models.CharField(max_length=500)
    year = models.CharField(max_length=100)