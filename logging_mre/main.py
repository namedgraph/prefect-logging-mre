import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

def main():
    start_time = time.time()
    while time.time() - start_time < 10:
        logger.info("Logging something every second")
        time.sleep(1)

if __name__ == "__main__":
    main()
