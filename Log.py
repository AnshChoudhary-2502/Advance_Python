import logging
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w" , format= "%(asctime)s - %(levelname)s - %(message)s")
# level shows the required logging levels
# filename shows in which file all logging should be stored
# filemode shows the operation on .log file
# format shows in what format logging should be shown in file
logging.debug("Debug")                       # 10
logging.info("Info")                         # 20
logging.warning("Warning")                   # 30
logging.error("Error")                       # 40
logging.critical("Critical")                 # 50
