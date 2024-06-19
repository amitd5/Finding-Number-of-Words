def count_words(text):
    """
    This function takes a string input and returns the count of words.
    A word is defined as any sequence of characters separated by whitespace.
    """
    # Split the text into words based on whitespace
    words = text.split()
    # Return the length of the list of words
    return len(words)

def main():
    """
    Main function to handle user input and output the word count.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Count the number of words in the input
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"The number of words in the input text is: {word_count}")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
