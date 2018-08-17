import chardet

def init(file):
    with open (file,'rb') as f:
        f = f.read()
        enc = chardet.detect(f)
        text = f.decode(enc['encoding']).split()
    return text

def treatment(text):
    count = {}
    top10 = []
    for word in text:
        if len(word) > 6:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    top10 = sorted(count, key=count.get, reverse=True)[:10]
    return top10

def main():
    files = ['newsafr.txt','newscy.txt','newsfr.txt','newsit.txt']
    for file in files:
        print('Топ 10 слов длиннее 6 символов в файле {}:\n{}'.format(file,treatment(init(file))))

main()
