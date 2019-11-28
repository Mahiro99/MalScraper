from urllib.request import urlopen as request
from bs4 import BeautifulSoup as bs


anime_seasonal_url="https://myanimelist.net/anime/season/2019/summer"
connection=request(anime_seasonal_url)
seasonal_raw_html=connection.read()
connection.close()

parsed_html = bs(seasonal_raw_html,"html.parser")

main_container=parsed_html.find_all("div", {"class":"seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix"})
newAnimes=main_container[0]
newAnime_length=len(main_container[0])


container_animes= parsed_html.findAll("div", {"class":"seasonal-anime js-seasonal-anime"})
count=0

f=open("seasonalAnimeInfo.csv","w+", encoding="utf-8")
header="Title, Studio, Ratings\n"
f.write(header)

for animes in container_animes:
    if animes in main_container[0]:
        if count<newAnime_length:
            numOne = container_animes[count]
            count+=1
            title_searcher=numOne.findAll("a",{"class":"link-title"})
            title_name=title_searcher[0].text.replace(","," ")

            producer_searcher=numOne.find("div",{"class":"prodsrc"})
            emptyOrNot= producer_searcher.span.text.strip()
            if emptyOrNot=="-":
                studio="Studio not Found"
            else:
                studio=producer_searcher.a["title"]

            rating_searcher=numOne.find("span",{"class":"score"})
            ratings=rating_searcher.text.strip()

            print(title_name)
            print(studio)
            print(ratings)
            print()
            f.write(title_name + "," + studio + "," + ratings+"\n")
f.close()