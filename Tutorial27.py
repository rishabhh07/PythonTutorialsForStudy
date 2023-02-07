# Time module in python
# My Practice
import time
# Time_since=time.time()
# print("This is time since 1st jan 1970 :",Time_since)
# time.asctime()

initial= time.time()
print(initial)
R=0
while (R<45):
    print("Rishabh is a good boy")
    # time.sleep()
    R+=1

time.sleep(5)
print(f"This is time of while loop : {time.time()-initial} Seconds")


# initial2=time.time()
# print("\nAstey Boliyega\n")
# for s in range(45):
#     print("Rishabh is a good boy")
# print(f"This is time of For loop : {time.time()-initial2} Seconds")

Current_Time=time.asctime(time.localtime(time.time()))
print(Current_Time)


# Harry description
# import time
# seconds = time.time()
# print("Seconds since epoch =", seconds)
# time.asctime()
#
#
#
# time.sleep(5)
#
#
# time.localtime([ sec ])
#
#
#
# import time
#
# print "time.localtime() returns: %s",%time.localtime()
#
#
#
# # Code file as described in the video
# import time
#
# initial = time.time()
#
# k = 0
# while (k < 45):
#     print("This is harry bhai")
#     time.sleep(2)
#     k += 1
# print("While loop ran in", time.time() - initial, "Seconds")
#
# initial2 = time.time()
# for i in range(45):
#     print("This is harry bhai")
# print("For loop ran in", time.time() - initial2, "Seconds")
#
# # localtime = time.asctime(time.localtime(time.time()))
# # print(localtime)

