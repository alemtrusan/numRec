"""
Main entry point for the numRec application.
Starts the GUI for handwritten digit recognition.
"""

from functions import App

if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")