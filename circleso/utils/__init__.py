# utils.py
# author: Container Nerds LLC.

# Python dependencies
import os
import sys

def preflight_checks():
    
    # Ensure Python 3.5 or higher
    if sys.version_info <= (3, 5):
        print('This script requires Python 3.5 or higher.')
        sys.exit(1)

    if os.getenv('CIRCLESO_API_KEY') is None:
        print('CIRCLESO_API_KEY environment variable not set.')
        sys.exit(1)
