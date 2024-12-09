import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

is_first_execution = True        # Variable to track if the Lambda function is executing for the first time (cold start)

environment_initialization_time = time.time()

time.sleep(20)       # Simulate a long initialization process (e.g., loading resources or dependencies)

def lambda_handler(event, context):
    global is_first_execution
    function_execution_start_time = time.time()

    # Check if this is the first invocation (cold start) or subsequent invocations (warm start)
    if is_first_execution:
        initialization_duration = function_execution_start_time - environment_initialization_time       # Cold start: Initialize the function and calculate the initialization duration
        logger.info(
            f"Cold start detected! The environment initialization took {initialization_duration:.4f} seconds. "
            f"The Lambda function is now ready for processing."
        )
        is_first_execution = False       # Set to False after the first execution to indicate warm starts
    else:
        logger.info(
            "Warm start detected! Reusing the pre-initialized Lambda environment."      # Lambda is in warm state
        )
        
    logger.info("Executing business logic...")       # Simulate processing time. Actual Business logic code goes here...    
    time.sleep(30)
    logger.info("Business logic executed successfully.")        # End of the business logic
        
    function_execution_end_time = time.time()        # Record the end time of the function execution
    execution_duration = function_execution_end_time - function_execution_start_time
    logger.info(
        f"The Lambda handler completed execution. Total execution time: {execution_duration:.4f} seconds."
    )

    return {
        "statusCode": 200,
        "body": f"The Lambda function executed successfully in {execution_duration:.4f} seconds."
    }
