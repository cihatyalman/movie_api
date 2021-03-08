from Core.utilities.results.data_result import DataResult

class SuccessDataResult(DataResult):

    def __init__(self, data=None, message=""):
        super().__init__(True, data, message)
