import requests
from bs4 import BeautifulSoup

from DataAccess.database_managers.language_dal import LanguageDal
from DataAccess.database_managers.category_dal import CategoryDal
from DataAccess.database_managers.link_dal import LinkDal
from Entities.movie import Movie
from Entities.link import Link

class WebScrapingManager:
    language_dal = LanguageDal()
    category_dal = CategoryDal()
    link_dal = LinkDal()

    __baselink = "https://wfilmizle.pw/page/"

    @classmethod
    def get_language_index(cls,language):
        try:
            for l in cls.language_dal.languages:
                r = language.find(l)
                if(r!=-1):
                    return cls.language_dal.languages.index(l)+1
            return -1
        except:
            return -1
    
    @classmethod
    def get_category_indexes(cls,category_list):
        result_list = []
        for c in category_list:
            try:
                result_list.append(cls.category_dal.categories.index(c)+1)
            except:
                continue
        return result_list

    @classmethod
    def get_link(cls,page_count):
        page_number_list = list(range(1,page_count+1))
        page_number_list.reverse()

        link_datas = []

        for index in page_number_list:
            try:
                soup = BeautifulSoup(requests.get(cls.__baselink+str(index)).content,"html.parser")
                soup_data = soup.find_all("div",{"class":"icerik"})[0]
                data_list = list(soup_data.find_all("div",{"class":"frag-k"}))
                data_list.reverse()

                for data in data_list:
                    try:
                        link_data=Link()
                        link_data.name = data.a["title"].strip().replace(" izle","")
                        link_data.link = data.a["href"]
                        link_datas.append(link_data)
                    except:
                        continue

                print("( {} / {} ) : Page {} completed.".format(str(index),str(len(page_number_list)),str(index)))
            except:
                continue
        return link_datas

    @classmethod
    def get_movie_detail(cls,link_index=0):
        try:
            link_datas = cls.link_dal.get("WHERE id>{}".format(link_index))
            movie_list=[]

            for link_data in link_datas:
                try:
                    movie_data = Movie()
                    movie_data.name = link_data.name
                    movie_data.link = link_data.link

                    soup = BeautifulSoup(requests.get(link_data.link).content,"html.parser")
                    soup_data = soup.find_all("div",{"class":"f-bilgi"})[0]

                    try:
                        imdb = float(soup_data.div.div.span.text.strip())
                    except:
                        imdb = float(0)
                    movie_data.imdb = imdb
                    movie_data.image = soup_data.find_all("div",{"class":"afis"})[0].img["src"]
                    _language = soup_data.find_all("span",{"class":"sol"})[0].text.strip()
                    movie_data.language_index = cls.get_language_index(_language)
                    movie_data.subject = soup_data.find_all("div",{"class":"aciklama"})[0].div.text.strip()
                    movie_data.year = int(soup_data.find_all("div",{"class":"bilgi"})[0].find_all("div",{"class":""})[0].a.text.strip().replace(" Filmleri izle",""))
                    _categories_data = soup_data.find_all("div",{"class":"bilgi"})[0].find_all("div",{"class":""})[1].find_all("a")
                    _categories = [" ".join(x.text.strip().split(" ")[:-2]) for x in _categories_data]
                    movie_data.category_indexes = "-".join(str(e) for e in cls.get_category_indexes(_categories))

                    movie_list.append(movie_data)
                    print("( {} / {} ) : '{}' details received.".format(str(link_datas.index(link_data)+1),str(len(link_datas)),link_data.name))
                except:
                    continue
            return movie_list
        except:
            return []
