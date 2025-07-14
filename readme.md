# numRec

Handwritten Digit Recognition using a Convolutional Neural Network (CNN) and a graphical user interface (GUI).


<img width="336" height="368" alt="Captura de pantalla 2025-07-14 220535" src="https://github.com/user-attachments/assets/27d6595c-049c-4bf7-9002-8e4d166b8f60" />   <img width="338" height="365" alt="Captura de pantalla 2025-07-14 220916" src="https://github.com/user-attachments/assets/07efcbc1-63ae-4bc5-85ce-fd8378c80b7f" />


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

