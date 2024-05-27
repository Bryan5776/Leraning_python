from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import numpy as np

def scale_dataset(dataframe, oversample=True):
  X = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(X)

#la cantidad de gammas y hadrons no es la misma y eso puede ser un problema so 
#7419 vs 3993
  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)


#hstack pone los arrays juntos horizontalmente 

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y