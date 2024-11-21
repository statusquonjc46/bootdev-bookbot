def main():
    print(count_words(file_contents))
    print(count_chars(file_contents))

def count_words(text):
    return len(text.split())

def count_chars(text):
    out_dict = {}
    lower_txt = text.lower()
    for c in lower_txt:
        if c not in out_dict:
            out_dict[c] = 1
        else:
            out_dict[c] += 1
    return out_dict

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    f.close()

main()