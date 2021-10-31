from urllib.request import urlopen as request
from bs4 import BeautifulSoup as bs
from datetime import date, datetime

#test
seasonInput = input("Enter Season: ")
seasonInput=seasonInput.lower()

yearInput= input("Enter the Year: ")

day = datetime.today().timetuple().tm_yday

spring = range(80, 172)
summer = range(172, 264)
fall = range(264, 355)
winter=range(355,80)


def findSeason(seasonInput):
    if day in spring and seasonInput == spring:
        anime_seasonal_url="https://myanimelist.net/anime/season"
        return makeItWork(anime_seasonal_url)

    elif day in summer and seasonInput == summer:
        anime_seasonal_url="https://myanimelist.net/anime/season"
        return makeItWork(anime_seasonal_url)

    elif day in fall and seasonInput == fall:
        anime_seasonal_url="https://myanimelist.net/anime/season"
        return makeItWork(anime_seasonal_url)

    elif day in winter and seasonInput == winter:
        anime_seasonal_url="https://myanimelist.net/anime/season"
        return makeItWork(anime_seasonal_url)

    else:
        anime_seasonal_url="https://myanimelist.net/anime/season/" +yearInput +"/" +seasonInput
        return makeItWork(anime_seasonal_url)


def makeItWork(anime_seasonal_url):
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

findSeason(seasonInput)
