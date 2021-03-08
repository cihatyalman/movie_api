from Core.utilities.results.error_result import ErrorResult
from Core.utilities.results.error_data_result import ErrorDataResult
from Business.constants.constant import Constant

class DecoratorHelper:

    @staticmethod
    def exception_func_for_check_error_with_data(*args): return ErrorDataResult().toMap()

    @staticmethod
    def exception_func_for_check_error(*args): return ErrorResult().toMap()
    