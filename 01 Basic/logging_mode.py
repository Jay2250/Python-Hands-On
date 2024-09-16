import logging

# Configure the logger globally
logging.basicConfig(
    filename='basicConfig2.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_execution(mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('advancedConfig_logger2')
            handler = logging.FileHandler('advancedConfig2.log')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            if not logger.hasHandlers():
                logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)

            # Determine logging level based on `mode`
            if mode == 'debug':
                logger.debug(f'{func.__name__} has begun')
                result = func(*args, **kwargs)
                logger.debug(f'{func.__name__} has ended')
            elif mode == 'info':
                logger.info(f'{func.__name__} has begun')

                result = func(*args, **kwargs)
                logger.info(f'{func.__name__} has ended')
            elif mode == 'error':
                logger.error(f'{func.__name__} has begun')
                result = func(*args, **kwargs)
                logger.error(f'{func.__name__} has ended')
            else:
                print('Give appropriate mode input')
                result = func(*args, **kwargs)  # Still call function if mode is invalid

            return result

        return wrapper
    return decorator

# Apply the decorator with mode as an argument
@log_execution('error')
def greet(name):
    print(f'Hello {name}...!')
    for i in range(1000):
        print(i, end=" ")

# Call the decorated function
greet('Jay')
