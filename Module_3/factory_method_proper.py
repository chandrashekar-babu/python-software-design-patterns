def create_logger(url):      # External / Outer function
 
    if url.startswith("http"):
        def logger():  # Inner function
            print("Logging using HTTP protocol")

    elif url.startswith("mysql:"):
        def logger():
            print("Logging to MySQL database")

    elif url.startswith("file:"):
        def logger():
            print("Logging to Filesystem")
    return logger

if __name__ == '__main__':
    #logger = create_logger("http://localhost:4040/logapi")
    #logger = create_logger("mysql://localhost:3306/logdb")
    logger1 = create_logger("file:///var/log/logdata.log")
    logger2 = create_logger("http://localhost:4040/logapi")

    logger1()
    logger2()

