def consumer(name):
    while True:
        print("i want some food!")
        food = yield
        print("i am eating the food{}!".format(food))
def producer(obj):
    obj.send(None)
    for i in range(10):
        print('making the food{}!'.format(i))

        obj.send(i)


producer(consumer('qiyaming'))