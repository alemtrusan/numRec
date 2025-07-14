from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from PIL import Image, ImageDraw
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tkinter as tk

model = load_model('models/mnist_cnn.keras')
def show_image(x_train, y_train,i):
    plt.imshow(x_train[i],cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.show()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Draw a Digit")
        self.resizable(False, False)

        self.canvas_size = 280  # Big canvas for easy drawing
        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)  # White background
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        button_frame = tk.Frame(self)
        button_frame.pack()

        tk.Button(button_frame, text="Predict", command=self.predict_digit).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Clear", command=self.clear_canvas).pack(side=tk.LEFT)

        self.result_label = tk.Label(self, text="", font=("Arial", 18))
        self.result_label.pack()

    def paint(self, event):
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")
        self.draw.ellipse([x1, y1, x2, y2], fill=0)  # Draw on the image too

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_size, self.canvas_size], fill=255)
        self.result_label.config(text="")

    def predict_digit(self):
        # Convert to 28x28 like MNIST
        img_resized = self.image.resize((28, 28))
        img_array = np.array(img_resized)
        img_array = 255 - img_array  # Invert: white bg -> black bg
        img_array = img_array / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        prediction = model.predict(img_array)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)

        self.result_label.config(text=f"Predicted: {digit} (Confidence: {confidence:.2f})")