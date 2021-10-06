class Headers(object):
    _instance = None

    def __new__(cls, args, *kwargs):
        # print(cls._instance)
        # print(args)
        if not cls._instance:
            cls._instance = args
        return cls._instance


class Response(object):
    _instance = None

    def __new__(cls, args, *kwargs):
        if not cls._instance:
            cls._instance = args[0]
        return cls._instance
