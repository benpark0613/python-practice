import time

# def myfunc():
#     start = time.time()
#     print("함수 실행")
#     end = time.time()
#     print("함수 수행시간: %f 초" % (end - start))
#
# myfunc()

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초 " % (end - start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수 실행")

# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()