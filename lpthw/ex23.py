import sys
script,encoding,error = sys.argv


def main(language_file,encoding,errors):
    line = language_file.readline()
    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)
    return None


def print_line(line,encoding,errors):
    next_language = line.strip()
    raw_bytes = next_language.encode(encoding,errors = errors)
    cooked_str = raw_bytes.decode(encoding,errors = errors)

    print(raw_bytes," <==> ",cooked_str)
    return None


languages = open("languages.txt",encoding = "utf-8")

main(languages,encoding,error)
