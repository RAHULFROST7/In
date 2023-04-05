import tkinter as tk
import webview

root = tk.Tk()
root.geometry("800x600")

# Create a new web browser window
browser = webview.create_window("My Browser", "https://www.google.com")

# Run the main event loop
webview.start()

root.mainloop()