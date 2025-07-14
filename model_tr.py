from functions import *

# Load the MNIST dataset (training and test images and labels)
(x_train,y_train),(x_test,y_test) = mnist.load_data()

# Normalize input data and reshape for the CNN
x_train = x_train / 255.0
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test / 255.0
x_test = x_test.reshape(-1,28,28,1)

# Convert labels to one-hot encoding
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

# Define the CNN model architecture
model = Sequential([
    Conv2D(32, kernel_size=(3,3),activation="relu",input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, kernel_size=(3,3),activation="relu"),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128,activation="relu"),
    Dropout(0.5),
    Dense(10,activation="softmax")
])

# Compile the model with optimizer and loss function
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

# Train the model with training data
model.fit(x_train,y_train,epochs=50,batch_size=32,validation_split=0.1)

# Evaluate the model on test data and print results
loss, accuracy = model.evaluate(x_test,y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

# Save the trained model in the 'models' folder
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)
model.save(os.path.join(model_dir, "mnist_cnn.keras"))
