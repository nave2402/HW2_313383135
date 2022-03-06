# Task 1

def reverse(sentence=None, reverse_word=None):
    # Makes sure I get string input
    if type(sentence) != str or type(reverse_word) != str:
        return "Invalid input detected"
    else:
        try:  # Check if the 'reverse word' is in the sentence
            if reverse_word not in sentence:
                return "The word was not found"
            else:  # Reverse word in sentence
                sentence = sentence.replace(reverse_word, reverse_word[::-1], 1)
                return sentence
        except:
            return "Invalid input detected"


# print(reverse("I like apples and I also like bananas", "like"))


# Task 2

def compute_equation(equation=None):
    try:
        x = eval(equation)
        return x
    except:
        return "invalid input detected"

# print(compute_equation("5*2+1-6^5+0.5"))
# print(type(compute_equation("5*2+1-6^5+0.5")))