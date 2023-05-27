from initializing import CheckNumbers

if __name__ == "__main__":

    curect = False

    print("""Hello welcome to youtube downloader \n
            1 : a video Download \n
            2 : Playlist Download \n
            3 : exit
          """)

    try:
        selectnumber = int(input("please select a number : "))
        curect = True
    except Exception:
        print('not a number!\n   try again.')

    if curect == True:
        CheckNumbers(selectnumber)

else:
    print('please run TYdownloader')
