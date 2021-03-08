class DecoratorBase:

    @staticmethod
    def on_before(deco_func):
        "deco_func: func(*args)"
        def wrap(original_func):
            def wrapped_f(*func_args):
                deco_func(*func_args)
                result = original_func(*func_args)
                return result
            return wrapped_f
        return wrap

    @staticmethod
    def on_after(deco_func):
        "deco_func: func(result,*args)"
        def wrap(original_func):
            def wrapped_f(*func_args):
                result = original_func(*func_args)
                deco_func(result,*func_args)
                return result
            return wrapped_f
        return wrap

    @staticmethod
    def on_exception(error_func):
        "error_func: return func(*args)"
        def wrap(original_func):
            def wrapped_f(*func_args):
                try:
                    result = original_func(*func_args)
                except:
                    result = error_func(*func_args)
                finally:
                    return result
            return wrapped_f
        return wrap
