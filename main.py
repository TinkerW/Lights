# from threading import Thread
# import time
#
# def red():
#     while True:
#         print("Красный")
#         time.sleep(10)
#
#
#
# def yellow():
#     while True:
#         time.sleep(5)
#         print("Жёлтый")
#     time.sleep(5)
#
#
#
# def green():
#     while True:
#         time.sleep(10)
#         print("Зелёный")
#         time.sleep(10)
#
#
# redlight = Thread(target=red, args=())
# yellowlight = Thread(target=yellow, args=())
# greenlight = Thread(target=green, args=())
# redlight.start()
# yellowlight.start()
# greenlight.start()