import sys
from news_data import TextData
from wordcloud import WordCloud
import MeCab as mecab

def GenerateWordCloud(option):
    
    word = WordCloud(background_color="white",
    font_path="./ipag.ttf",
    width=1000,height=800)

    if len(option) < 2:

        return word.generate(str(TextData()).replace("'", ""))

    elif option[1] == "-mecab":
        
        return word.generate(''.join(WordList()))

    else:
        print("引数が無効です")
        sys.exit()

def WordList():

    m = mecab.Tagger("-Ochasen")
    wordList = []
    textData = TextData()

    for line in textData:
        node = m.parseToNode(line)

        while node:
            if len(node.surface) != "":
                wordType = node.feature.split(",")[0]
                if wordType in ["動詞", "形容詞","名詞"]:
                    wordList.append(node.surface + "\n")

            node = node.next
            if node is None:
                break

    print("mecabを利用して形態素解析を行っています\n")

    return wordList
