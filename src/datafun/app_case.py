"""src/datafun/app_case.py - Project script (example).

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

Terminal command to run this file from the root project folder

    uv run python -m datafun.app_case

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.

COURSE_NAME: Final[str] = "Data Analytics Fundamentals"
COURSE_NUMBER: Final[int] = 608
COURSE_HOURS_PER_WEEK: Final[float] = 20.0
ASSUMES_PRIOR_EXPERIENCE: Final[bool] = False
USES_PROFESSIONAL_PYTHON: Final[bool] = True
HELPFUL_TRAITS: Final[list[str]] = [
    "patience",
    "curiosity",
    "humor",
    "tenacity",
]

# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    summary: str = f"""
    Course Information:
        Course name: {COURSE_NAME}
        Course number: {COURSE_NUMBER}
        Course hrs/wk: {COURSE_HOURS_PER_WEEK:.2f}
        Assumes prior experience: {ASSUMES_PRIOR_EXPERIENCE}
        Uses Professional Python: {USES_PROFESSIONAL_PYTHON}
        Helpful traits: {HELPFUL_TRAITS}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    snowfall_inches: list[float] = [2.5, 3.5, 4.5, 5.5, 6.5]

    # Calculate descriptive statistics.
    total: float = sum(snowfall_inches)
    count: int = len(snowfall_inches)

    minimum: float = min(snowfall_inches) if count > 0 else 0.0
    maximum: float = max(snowfall_inches) if count > 0 else 0.0

    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0
    std_dev: float = statistics.stdev(snowfall_inches) if count > 1 else 0.0

    # Build a formatted multi-line string using f and triple quotes.
    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f} inches
        Maximum snowfall: {maximum:.2f} inches
        Average snowfall: {average:.2f} inches
        Standard deviation: {std_dev:.2f} inches
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).

    Arguments: None.
    Returns: None.
    """
    # Log a header for the application.
    log_header(LOG, "P01")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# This is standard Python "boilerplate".

if __name__ == "__main__":
    main()
