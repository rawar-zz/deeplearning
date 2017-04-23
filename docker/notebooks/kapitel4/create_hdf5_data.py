import h5py
import numpy as np

train_filename = 'xor_data.hdf5'
#data = np.array(((0, 0), (0, 1), (1, 0), (1, 1)))
data = np.array([[0,0], [0,1], [1,0], [1,1]])
print(data)
labels = np.array([0, 1, 1, 0])
print(labels)
with h5py.File(train_filename, 'w') as f:
    f['data'] = data.astype(np.float32)
    f['label'] = labels.astype(np.float32)
