import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D

# Define input shape
input_shape = (224, 224, 3)

# Define the CNN model
model = tf.keras.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(256, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
])

# Define a sample input image
img = np.random.rand(1, 224, 224, 3).astype(np.float32)

# Get the feature maps output by the model for the input image
feature_maps = model.predict(img)
print(feature_maps.shape)
