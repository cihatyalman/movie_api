import requests
from bs4 import BeautifulSoup

from DataAccess.database_managers.link_dal import LinkDal
from DataAccess.database_managers.movie_dal import MovieDal
from Business.web_scraping.web_scraping_manager import WebScrapingManager

from Core.utilities.results.success_result import SuccessResult
from Core.utilities.results.success_data_result import SuccessDataResult
from Core.utilities.decorators.decorator import Decorator
from Business.helpers.decorator_helper import DecoratorHelper

class ApiManager:
    link_dal = LinkDal()
    movie_dal = MovieDal()

    @classmethod
    def __update_links(cls,page_count):
        result = cls.link_dal.get("LIMIT 1",True)[0]

        link_datas =  WebScrapingManager().get_link(page_count)
        continue_index = 0
        for index in range(len(link_datas)):
            if(link_datas[index]["name"] == result.name):
                continue_index = index+1
                break

        new_link_datas = link_datas[continue_index:]
        cls.link_dal.add_list(new_link_datas)

    @classmethod
    def __update_movies(cls):
        movie_id = cls.movie_dal.get_end_id()
        new_movie_list = WebScrapingManager().get_movie_detail(movie_id)
        cls.movie_dal.add_list(new_movie_list)

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error)
    def update_system(cls,page_count):
        cls.__update_links(page_count)
        cls.__update_movies()
        return SuccessResult.toMap()

    @classmethod    
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_all_movie(cls):
        result_list = cls.movie_dal.get("",True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_between_indexes_movie(cls,begin_index=0,end_index=10):
        end_id = cls.movie_dal.get_end_id()
        if(end_id>end_index and begin_index<end_index):
            where_code = "WHERE id<={} AND id>={}".format(end_id-begin_index,end_id-end_index)
        else:
            raise Exception()
        result_list = cls.movie_dal.get(where_code,True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_language_movie(cls,language_id):
        result_list = cls.movie_dal.get("WHERE language_index={}".format(language_id),True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_category_movie(cls,category_id):
        where_code="""WHERE category_indexes LIKE '{id}' OR category_indexes LIKE '{id}-%' 
        OR category_indexes LIKE '%-{id}' OR category_indexes LIKE '%-{id}-%' """.format(id=category_id)
        result_list = cls.movie_dal.get(where_code,True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_imdb_movie(cls,imdb):
        result_list = cls.movie_dal.get("WHERE imdb>={}".format(imdb),True)
        return SuccessDataResult(result_list).toMap()
        
    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_year_movie(cls,year):
        result_list = cls.movie_dal.get("WHERE year>={}".format(year),True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_name_movie(cls,name):
        result_list = cls.movie_dal.get("WHERE name LIKE '%{}%'".format(name),True)
        return SuccessDataResult(result_list).toMap()
    
    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_id_movie(cls,id):
        result_list = cls.movie_dal.get("WHERE id={}".format(id),True)
        return SuccessDataResult(result_list).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.exception_func_for_check_error_with_data)
    def get_by_custom_code(cls,sql_code):
        result_list = cls.movie_dal.get_custom_code(sql_code)
        return SuccessDataResult(result_list).toMap()
