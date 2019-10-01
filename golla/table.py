class BaseChild:
    Connection = None

    def __init__(self):
        super()

    def get_by_id(self, **kwargs):
        try:
            if len(kwargs) == 1:
                key, value = list(kwargs.items())[0]
                return self.Connection.query(self.__class__).filter(getattr(self.__class__, key) == value).one()
            else:
                raise Exception("Multiple ids will not support")
        except Exception as e:
            raise Exception(e)

    def get_by_ids(self, **kwargs):
        pass

    def get_all(self):
        try:
            return self.Connection.query(self.__class__).all()
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def save(obj):
        try:
            BaseChild.Connection.add(obj)
            BaseChild.Connection.commit()
        except Exception as e:
            BaseChild.Connection.rollback()
            raise Exception(e)

    def delete_by_id(self, **kwargs):
        try:
            if len(kwargs) == 1:
                key, value = list(kwargs.items())[0]
                self.Connection.query(self.__class__).filter(getattr(self.__class__, key) == value).delete()
                self.Connection.commit()
                return True
            else:
                raise Exception("Multiple ids will not support")
        except Exception as e:
            self.Connection.rollback()
            raise Exception(e)
