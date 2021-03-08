from DataAccess.database_managers.language_dal import LanguageDal
from DataAccess.database_managers.category_dal import CategoryDal
from DataAccess.database_managers.link_dal import LinkDal
from DataAccess.database_managers.movie_dal import MovieDal
from Business.web_scraping.web_scraping_manager import WebScrapingManager

class ApiHelper:
    language_dal = LanguageDal()
    category_dal = CategoryDal()
    link_dal = LinkDal()
    movie_dal = MovieDal()
    
    @classmethod
    def api_configure(cls):
        "Run Once !"

        cls.language_dal.configure()
        cls.category_dal.configure()

        link_datas = WebScrapingManager().get_link(2)
        cls.link_dal.add_list(link_datas)

        movie_list = WebScrapingManager().get_movie_detail()
        cls.movie_dal.add_list(movie_list)
