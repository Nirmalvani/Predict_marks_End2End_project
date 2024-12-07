"""
It allows you to define custom exceptions for specific errors in your application. 
By raising and catching specific exceptions, you can create more granular error-handling flows.
"""

import sys
import logging
from src.logger import logging

# Custom Exception Base Class
class MLBaseError(Exception):
    """Base class for all exceptions in the ML project."""
    pass

# Specific custom exception classes for different error types
class DataLoadingError(MLBaseError):
    """Raised when there is an issue with loading the dataset."""
    pass

# Function to handle exceptions and log details
def handle_exception(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error occurred in file '{file_name}', line {line_number}: {error}"

    # Log the error message
    logging.error(error_message)
    
    # Print error message to console as well
    print(error_message)
