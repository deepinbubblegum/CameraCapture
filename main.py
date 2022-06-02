from PiRecord import CaptureMode, FileServer

if __name__ == "__main__":
    cap_ = CaptureMode()
    cap_.start()
    serv_ = FileServer()
    serv_.start()