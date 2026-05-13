def create_logger(url):      # External / Outer function
    global logger
    
    if url.startswith("http"):
        def logger():  # Inner function
            print("Logging using HTTP protocol")

    elif url.startswith("mysql:"):
        def logger():
            print("Logging to MySQL database")

    elif url.startswith("file:"):
        def logger():
            print("Logging to Filesystem")

if __name__ == '__main__':
    #create_logger("http://localhost:4040/logapi")
    #create_logger("mysql://localhost:3306/logdb")
    create_logger("file:///var/log/logdata.log")

    logger()

