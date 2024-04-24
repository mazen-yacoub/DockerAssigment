
import re
from collections import Counter

# Open the file in read mode ("r")
with open("random_paragraphs.txt", "r") as file:
  text = file.read()

# Define stop words
StopWords = [
    "a", "an", "the", "of", "is", "in", "on", "to", "for", "as", "with", "by",
    "at", "which", "be", "have", "it", "that", "this", "are", "from", "or",
    "your", "our", "those", "such", "too", "my", "ones", "would", "them", "and"
]

# Convert text to lowercase and remove punctuation
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

# Split the text into words
words = text.split()

# delete stop words
filtered_words = [word for word in words if word not in StopWords]

# Combine filtered words with spaces
new_text = " ".join(filtered_words)

# Write the filtered text back to the file
with open("random_paragraphs.txt", "w") as file:
    file.write(new_text)

# Print the filtered text
print("Filtered text:")
print(new_text)

# Count the frequency of each word in the filtered text
word_counts = Counter(filtered_words)

# Display the word frequency count to the console
print("\nWord frequency count:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

