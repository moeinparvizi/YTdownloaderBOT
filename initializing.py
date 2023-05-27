from pytube import Playlist


def OperationOne():
    print("operation1")

def OperationMany():
    link = input("enter your youtube Playlist URL : ")
    yt_playlist = Playlist(link)

    path = input("enter your path : ")

    for video in yt_playlist:
        video.streams.get_lowest_resolution().download(path)
        print("Video Downloaded: ",video.title)

    print("\nAll Videos are Downloaded.")

def CheckNumbers(selectnumber):
    match selectnumber:
        case 1:
            OperationOne()
        case 2:
            OperationMany()
        case 3:
            print("goodbye!")
            exit()
        case _:
            print("your number not define!\n    try again.")
