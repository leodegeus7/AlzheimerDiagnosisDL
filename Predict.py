
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Activation, Dropout
from keras import backend as K
import os


# In[2]:


epochs = 50
batch_size = 16

img_width, img_height = 257, 170

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)


# In[3]:


input_shape


# In[4]:


classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape=input_shape))
classifier.add(Activation('relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(32, (3, 3)))
classifier.add(Activation('relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(64, (3, 3)))
classifier.add(Activation('relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Flatten())
classifier.add(Dense(64))
classifier.add(Activation('relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(1))
classifier.add(Activation('sigmoid'))

classifier.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


# In[5]:


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('ProcessedImage/training_set',
                                                 target_size = (img_width, img_height),
                                                 batch_size = batch_size,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('ProcessedImage/test_set',
                                            target_size = (img_width, img_height),
                                            batch_size = batch_size,
                                            class_mode = 'binary')


# In[9]:


nb_train_samples = 512
nb_validation_samples = 51

classifier.load_weights(os.getcwd() + "/" + "model.h5")

t1 = nb_train_samples // batch_size
t2 = nb_validation_samples // batch_size


# In[ ]:


losstest = classifier.fit_generator(
                    training_set,
                    steps_per_epoch=t1,
                    epochs=epochs,
                    validation_data=test_set,
                    validation_steps=t2)


# In[8]:


directory = os.getcwd()
h5File = directory + "/model.h5"
classifier.save_weights(h5File)


# In[13]:


scores = classifier.evaluate_generator(test_set) #1514 testing images
print("Accuracy = ", scores[1])


# In[ ]:


classifier.hi

