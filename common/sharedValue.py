import threading

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class getInstance:
    lock=threading.Lock()
    thisDict={"count" : 0, "run" : 0}

    def __init__(self) -> None:
        pass

    def set(self, key, value):
        self.lock.acquire()
        try:
            self.thisDict[key] = value
        finally:
            self.lock.release()

    def get(self, key):
        self.lock.acquire()
        try:
            ret = self.thisDict[key]
        except KeyError:
            ret = -1
        finally:
            self.lock.release()
        return ret
    

