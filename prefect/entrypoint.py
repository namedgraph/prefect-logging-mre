import logging
import prefect
from prefect import flow
from logging_mre.main import main  # Import your script as a module

# Configure logging for the specific logger
extra_logger = logging.getLogger("logging_mre.main")
extra_logger.setLevel(logging.INFO)

# Define a sub-flow that calls main()
@flow(name="Sub Flow")
def sub_flow():
    logger = prefect.get_run_logger()
    logger.info("Calling main() from logging_mre.main as a sub-flow")

    # Call the function directly
    main()

# Define the main flow
@flow(name="Main Flow")
def main_flow():
    logger = prefect.get_run_logger()
    logger.info("Starting the main flow")
    
    # Execute the sub-flow
    sub_flow()

    logger.info("Main flow completed")

# Run the main flow when the script is executed
if __name__ == "__main__":
    main_flow()
