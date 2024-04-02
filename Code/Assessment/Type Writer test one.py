import time
import sys

# Function to create the typewriter effect
def typewriter_effect(sentence, type_delay, delete_delay):
    # Loop through each character in the sentence
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

    # Pause after printing the entire sentence
    time.sleep(1)

    # Loop to delete the sentence
    for _ in sentence:
        # Write backspace, space, delete and delay
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(delete_delay)

# List of sentences to display in typewriter effect
sentences = [
    "Hello, Reader! How are You?",
    "This is a console based typewriter effect.",
    "Using Python it simulates the appearance of a typewriter."
]

# Typing and Deleting speed in seconds
type_delay = 0.05
delete_delay = 0.01

while True:
    # Iterate over each sentence in the list
    for sentence in sentences:

        # Call the typewriter_effect function
        typewriter_effect(sentence, type_delay, delete_delay)

        # Print a carriage return to overwrite the sentence and 
        # start the next iteration with a clean console output
        print('\r', end='')