import logging
def log_to_file(log_file, log_level= logging.INFO):
    logging.basicConfig(
        filename = log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s 0- %(message)s'
    )
    def decorator(func):
        def wrapper(*args,**kwargs):
            logging.log(log_level, f'starting {func.__name__}...')
            result = func(*args,**kwargs)
            logging.log(log_level,f'Finished {func.__name__}.')
            return result
        return wrapper
    return decorator

    log_to_file('mylog.log')

# ----------------------------------------------------------------

import logging
logging.basicConfig(
    filename= 'basicConfig.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logger = logging.getLogger('advancedConfig_logger')
handler = logging.FileHandler('advancedConfig.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler,)
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


# ----------------------------------------------------------------

import logging
logging.basicConfig(
            filename= 'basicConfig1.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
def log_execution(func):
    def wrapper(*args,**kwargs):
        print(f"Before program execution...")

        logger = logging.getLogger('advancedConfig_logger1')
        handler = logging.FileHandler('advancedConfig1.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler,)
        logger.setLevel(logging.DEBUG)
        logging.info(f'\n{func.__name__} has begun')
        func(*args, **kwargs)
        logging.info(f'\n{func.__name__} has ended')
        print(f"\nAfter program execution...")

    return wrapper


@log_execution
def greet(name):
    print(f'Hello {name}...!')
    for i in range(1000):
        print(i, end=" " )
greet('Jay')
