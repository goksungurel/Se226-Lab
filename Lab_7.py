class StringUtils:
    
    def reverse_string(s):
        return s[::-1]


    def capitalize_words(s):
        return s.title()


    def remove_punctuation(s):
        return s.translate(str.maketrans('', '', string.punctuation))


    def count_characters(s):
        return len(s)


    def count_words(s):
        return len(s.split())


    def average_word_length(s):
        words = s.split()
        return sum(len(word) for word in words) / len(words) if words else 0

  class StringAnalyzer:
    def __init__(self):
        self.string_utils = StringUtils()

    def analyze(self):
        sentence = input("Enter a sentence: ")

    
        reversed_sentence = self.string_utils.reverse_string(sentence)
        capitalized_sentence = self.string_utils.capitalize_words(sentence)

      
        no_punctuation = self.string_utils.remove_punctuation(sentence)

       
        char_count = self.string_utils.count_characters(no_punctuation)
        word_count = self.string_utils.count_words(no_punctuation)

       
        avg_word_length = self.string_utils.average_word_length(sentence)

       
        print(f"Reversed sentence: {reversed_sentence}")
        print(f"Capitalized sentence: {capitalized_sentence}")
        print(f"Sentence without punctuation: {no_punctuation}")
        print(f"Character count (without punctuation): {char_count}")
        print(f"Word count: {word_count}")
        print(f"Average word length: {avg_word_length:.2f}")

    def run(self):
        if __name__ == "__main__":
            self.analyze()



calc = Calculator()
calc.run()


string_analyzer = StringAnalyzer()
string_analyzer.run()
