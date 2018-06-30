import logging
import sys

def app():
    app_logger = logging.getLogger("APP")
    app_logger.setLevel(logging.INFO)
    app_formater = logging.Formatter("%(name)s - %(asctime)s - %(filename)s: %(message)s")
    app_handler = logging.StreamHandler(sys.stdout)
    app_handler.setFormatter(app_formater)
    app_logger.addHandler(app_handler)

    app_logger.info("APP config ...")




def run():
    run_logger = logging.getLogger("APP.run")
    run_logger.setLevel(logging.INFO)
    run_formater = logging.Formatter("%(name)s - %(asctime)s - %(filename)s: %(message)s")
    run_handler = logging.StreamHandler()
    run_handler.setFormatter(run_formater)
    run_logger.addHandler(run_handler)
    run_logger.info("running now!")
    

def main():
    app()
    run()

if __name__ == '__main__':
    main()
