try:
    myFile= open("myData2.txt")

except FileNotFoundError as ex:
    print("that file was not found")    ##custom written error
    print(ex.args)                  ##built in error for the exception

else:
    print("File:",myFile.read())
    myFile.close()

finally:
    print("finish working with the file")


