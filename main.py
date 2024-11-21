def main():
    words = count_words(file_contents)
    chars = count_chars(file_contents)
    print(words)
    print(chars)

    create_report(words, chars)


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

def create_report(words, char_dict):
    report_header = f"""
--- Begin report of books/frankenstein.txt ---
{words} words found in the document
    """
    report_footer = f"--- End report ---"
    
    print(report_header)

    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for k in sorted_dict:
        if k.isalpha():
            print(f"The '{k}' character was found {sorted_dict[k]} times")
    
    print(report_footer)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    f.close()

main()