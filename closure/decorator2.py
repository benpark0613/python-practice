from closure.decorator import elapsed


@elapsed
def myfunc(msg):
    print("%s 출력." % msg)

myfunc("Ben")