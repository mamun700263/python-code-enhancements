# log_config.py
import logging

logger = logging.getLogger("username")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",    

)

# Create a file handler it shows in the terminal
# ch = logging.StreamHandler()
# ch.setFormatter(formatter)
# logger.addHandler(ch)

#this will show in the file
fh = logging.FileHandler("logger/user_manager.log") #location of the log file
fh.setFormatter(formatter)#this will show in the file
logger.addHandler(fh)

