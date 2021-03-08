from Core.utilities.results.result import Result

class DataResult(Result):

    def __init__(self, success, data=None, message=''):
        self.data = data
        super().__init__(success, message)

    def toMap(self):
        map = super().toMap()
        map["data"]=self.data
        return map