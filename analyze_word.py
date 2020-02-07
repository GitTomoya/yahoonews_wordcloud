from news_data import TitleText
from wordcloud import WordCloud

def GenerateWordCloud():
    
    word = WordCloud(background_color="white",
    font_path="./ipag.ttf",
    width=1000,height=800).generate(TitleText().replace("'",""))

    return word