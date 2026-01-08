# solution.py

def number_to_words(num):
    """
    Converts number to words: 270176 -> Two Seven Zero One Seven Six
    """
    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return ' '.join(words[int(d)] for d in str(num))

# Example usage (optional)
if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(number_to_words(num))