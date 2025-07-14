# numRec

Handwritten Digit Recognition using a Convolutional Neural Network (CNN) and a graphical user interface (GUI).

## Features

- Trains a CNN model on the MNIST dataset.
- Provides a GUI for digit recognition.


## Usage

1. **Train the model (optional):**
   ```
   python model_tr.py
   ```
   This will save the trained model in the `models` folder.

2. **Run the GUI application:**
   ```
   python main.py
   ```

## Project Structure

```
numRec/
│
├── main.py          # Starts the GUI application
├── model_tr.py      # Trains and saves the CNN model
├── functions.py     # Contains utility functions and App class
├── requirements.txt # Python dependencies
├── models/          # Saved models
│   └── mnist_cnn.keras
```