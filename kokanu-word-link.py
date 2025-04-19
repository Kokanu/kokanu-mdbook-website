import json
import sys
import re

def replace_dollar_sign_words(text):
    # Regular expression to match words that start with a dollar sign.
    pattern = r'\$(\w+)'
    # Replace the matched words with a link with text just being the word and the href being to the dictionary
    replaced_text = re.sub(pattern, r'[\1](https://dictionary.kokanu.com/\1?lang=en)', text)
    return replaced_text

def do_section (section):
    for chapter in section:
        section[chapter]["content"] = replace_dollar_sign_words(section[chapter]["content"])
    
        for sub_section in section[chapter]["sub_items"]:
            do_section(sub_section)

if __name__ == '__main__':
    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)

    print(json.dumps(book), file=sys.stderr)
    
    for section in book["sections"]:
        do_section(section)

    # we are done with the book's modification, we can just print it to stdout
    print(json.dumps(book))
