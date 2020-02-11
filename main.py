import sys
from analyze_word import GenerateWordCloud
from wordcloud import WordCloud
      
if __name__ == "__main__":

    i = sys.argv
    #pngファイルとして出力
    print("データを取得しています\n")
    print("------------------------------")

    out = GenerateWordCloud(i)
    out.to_file("./Wordcloud.png")

    print("------------------------------")
    print("\n画像ファイルが生成されました")

    sys.exit()

    
            

