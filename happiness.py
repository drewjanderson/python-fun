# Requires the web browser module to open the image and time...
import webbrowser
import time
import sys

# Define helper function to print the following print on the same line
def print_no_newline(string):
    sys.stdout.write(string)
    sys.stdout.flush()

# Wait for it
time.sleep(0.5)
print("   Wait for it")
print("   ")
time.sleep(1)

# Happiness...defined 
happiness = "yiss"
print_no_newline("   Aww ")
time.sleep(0.5)
print_no_newline(happiness)
time.sleep(1)
print_no_newline(".")
time.sleep(1)
print_no_newline(".")
time.sleep(1)
print_no_newline(".")
time.sleep(1)

# Opens CHEEZburger image
webbrowser.open_new("https://i.chzbgr.com/full/7856613376/hCC9312B2/")