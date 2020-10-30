import regex as rg

if __name__ == "__main__":
    file = open('gow.txt', 'r')
    theText = file.read().lower()

    # menerapkan regex untuk spasi, dan punctuation
    regex = "[a-zA-Z]+"

    # membuat variabel hasil
    resToken = rg.findall(regex, theText)

    # mencetak variabel hasil
    print(resToken, file=open('result.txt', 'a'))
    print(len(resToken))
