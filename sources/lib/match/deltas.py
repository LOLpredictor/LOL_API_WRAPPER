
class Deltas:
    def __init__(self):
       self.zero_ten = None
       self.ten_twenty = None
       self.twenty_thirty = None
       self.thirty_end = None


    @classmethod
    def data_to_object(cls, data):
        obj = cls()
        try:
            obj.zero_ten = data["0-10"]
        except:
            pass
        try:
            obj.ten_twenty = data["10-20"]
        except:
            pass
        try:
            obj.twenty_thirty = data["20-30"]
        except:
            pass
        try:
            obj.thirty_end = data["30-end"]
        except:
            pass

        return obj


    def to_dict(self):
        return self.__dict__