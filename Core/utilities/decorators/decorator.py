from Core.utilities.decorators.decorator_base import DecoratorBase
class Decorator(DecoratorBase):

    @staticmethod
    def default_before_func(*args):
        print("before: ", args)

    @staticmethod
    def default_after_func(result,*args):
        print("after: ", result, args)

    @staticmethod
    def default_exception_func(*args):
        print("error: ", args)
        return "ERROR"
