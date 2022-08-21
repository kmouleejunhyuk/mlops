from loguru import logger

def lam(x):
    return x ** 2


if __name__ == '__main__':
    for x in range(10):
        logger.info(lam(x))

    