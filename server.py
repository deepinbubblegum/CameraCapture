from camera import Record, FileServer
if __name__ == '__main__':
    rec = Record()
    file_ser = FileServer()
    rec.start()
    file_ser.start()