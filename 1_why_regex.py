import re


def main():
    txt = "It was a good idea. At least, they all thought it was a good idea at the time. Hindsight would reveal that in reality, it was an unbelievably terrible idea, but it would take another week for them to understand that. Right now, at this very moment, they all agreed that it was the perfect course of action for the current situation. John, however, was like 'What the...?'"

    # Search the txt for the value "the"
    x = re.search("the", txt) # This will create a "match object"
    print(x)
    print(x.span())
    print(txt[30:33])

    # re.search() only returns the FIRST match!

    # Use the re.findall() function to find all of the matches
    # This will return a list
    y = re.findall("the", txt)
    print('All instances of `the` in the text:')
    print(y) # Returns 7 occurrences, but includes "they", "them", and "another"
    print('\n')

    # Use findall to find all instances of the word "the"
    # \b finds matches at the beginning or end of a word
    y = re.findall(r"\bthe", txt)
    print('All instances of `the` at the beginning of a word:')
    print(y) # Got rid of the "the" in "another" but is still catching "they" and "them"
    print('\n')

    y = re.findall(r"\bthe\s", txt)
    print('All instances of `the` followed by a space.')
    print(y) # Gets the word "the" followed by a space, but misses the final "the"
    print('\n')

    y = re.findall(r"\bthe[a-z]", txt)
    print('All instances of `the` followed by another letter.')
    print(y) # Gets the word "the" followed by a space, but misses the final "the"
    print('\n')

    y = re.findall(r"\bthe[^a-z]", txt)
    print('All instances of `the` NOT followed by another letter.')
    print(y) # Gets the word "the" followed by a space, but misses the final "the"
    print('\n')

    y = re.findall(r"\b(the)[^a-z]", txt)
    print('Use a capture group to retrieve just the `the` portions of the text.')
    print(y) # All instances of "the" and no trailing characters

if __name__== "__main__":
  main()