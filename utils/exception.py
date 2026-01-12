from utils.logger import log
import traceback

def handle_exception(step_name, error):
    log(f"ERROR in {step_name}")
    log(f"Error Type: {type(error).__name__}")
    log(f"Error Message: {error}")
    log("Traceback:")
    log(traceback.format_exc())
