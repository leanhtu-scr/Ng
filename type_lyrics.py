import sys
import time

def type_text(text, delay=0.05):
    """Prints a string one character at a time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

lyrics = [
    "Ngay từ đầu em chẳng hề yêu anh",
    "Em chẳng hề yêu anh",
    "And I can't believe in love",
    "Em vẫn chưa hề quên được ai đó!",
    "Em vẫn đang còn nhớ về ai đó!",
    "Babe please don't don't hold me",
    "Babe please don't don't touch me"
]

# A larger delay to simulate a pause between lines
line_delay = 1.5

# Print the lyrics
for line in lyrics:
    type_text(line)
    time.sleep(line_delay)
