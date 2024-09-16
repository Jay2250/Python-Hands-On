import logging

logging.basicConfig(
    filename='basicConfig1.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Before program execution...")

        logger = logging.getLogger('advancedConfig_logger1')
        handler = logging.FileHandler('advancedConfig1.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler, )
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
        print(i, end=" ")


greet('Jay')