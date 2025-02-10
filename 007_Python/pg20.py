# try:
#     print(10+'50')
# except:
#     print("Something wrong")

try:
    print(int("4q"))
except TypeError:
    print("Something wrong \"Type Error\"")

except ValueError:
    print("Something wrong \"Value Error\"")

except ZeroDivisionError:
    print("Zerodivision error")

finally:
    print("Sucess")