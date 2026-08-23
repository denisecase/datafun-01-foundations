"""src/datafun/app.py - Project script.

Author: Denise Case
Date: 2026-08-20

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / New Terminal to
open an integrated Terminal in the root project folder.
Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m datafun.app

DOMAIN:

A dataset of penguins.
See docs/data-card.md for more information about the dataset.

EXPLORE:

The data is loaded from a CSV file in the data/ folder.
Open that CSV in Excel and look at it.
One row of data represents one penguin.
We can
- open Excel and explore data OR
- open an editor and write Python

With Python, the instructions are write once / use as many times
as we like, and we can copy the instructions to other projects.
Work can be stored in GitHub and shared with others.

ORGANIZATION:

This file is the main script for the project.
Execution begins at the start of the main() function.
We organize the instructions into different files
(a Python file is called a module).
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
from eda_vizkit import save_chart, show_numeric_relationship
import matplotlib.pyplot as plt
import pandas as pd

from datafun.utils_data import get_analyst_description, inspect

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P01", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT, # they do NOT change when the program runs.
# By convention, constants are named in # UPPERCASE_WITH_UNDERSCORES.
# `Final` is added to indicate these variables # should not be reassigned.

# === PATHS ARE IMPORTANT ===

# Clearly define relative paths to important items (like data files).
# The `Python Standard Library` is available in every Python project.

# One of the modules in the Python Standard Library is `pathlib`,
# which provides classes for handling filesystem paths.

# === LOCATE THE DATA FILE ===

# Use the Path() constructor to create a Path object representing the "data" folder.
# Combine with the CSV file name
# to get the full path to the data file.
DATA_FILE_PATH: Final[Path] = Path("data") / "penguins.csv"

# === OPEN THE DATA FILE IN EXCEL ===

# Look in the data/ folder. Open the file in Excel.
# Understand what is there and record your observations.

# === DETERMINE WHAT A ROW REPRESENTS ===

# CUSTOM: This is the GRAIN of the dataset - the single most
# important thing to know about any dataset.
# Come up with a short phrase that describes it.
# Fill this string value AFTER exploring the data.
GRAIN: Final[str] = "one penguin"  # CUSTOM

# === FIND A COLUMN YOU MIGHT BE ABLE TO PREDICT ===

# CUSTOM: Choose one NUMERIC target value that you might be able to predict
# from other columns in the dataset.
# This must match a numeric column name EXACTLY as it appears in the CSV file.
# I picked "body_mass_g" as the target column.
A_TARGET_WE_COULD_PREDICT: Final[str] = "body_mass_g"

# CUSTOM: Choose one other NUMERIC column
# as a FEATURE that might help predict the target.
# This must match a numeric column name EXACTLY as it appears in the CSV file.
# I picked "bill_length_mm" as the feature column.
A_FEATURE_THAT_MIGHT_HELP: Final[str] = "bill_length_mm"

# CUSTOM: Document your thinking.
# Why do you think that feature could help predict the target?
# I said the following.
# The `r`` in front of the string indicates a `raw` string,
# so it is very forgiving - it'll show up in the log
# like I typed it.
# Open and close with three double quotes to get a multi-line string.
WHY_THE_FEATURE_MIGHT_HELP: Final[str] = r"""
A bigger penguin probably has both a longer bill and more mass,
so bill length might help predict body mass.
That is, a longer bill may indicate a larger body mass.
"""


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    This is where the instructions begin.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P01")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    # Use the imported privacy-preserving log_path() function
    # To indicate where we will look for the data file.
    log_path(LOG, "data file", path=DATA_FILE_PATH)

    # Call the built-in pandas `read_csv` function.
    # Store the tabular pandas DataFrame returned
    # in a local variable named `df`.

    df: pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

    LOG.info("Data loaded successfully.")

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    # Call the inspect() function to get a string
    # with basic information about the DataFrame.
    # Pass in the pandas DataFrame (df)
    # The grain (what one row represents)
    # And the log so it knows where to send messages.

    inspection_string: str = inspect(df=df, grain=GRAIN, log=LOG)

    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. DESCRIBE the data.")
    LOG.info("-------------------------------")

    # Call the get_analyst_description function.
    # Pass in the variables defined above.
    # The function will return a string
    # with a summary of the data from the analyst's perspective.

    summary_string: str = get_analyst_description(
        grain=GRAIN,
        target=A_TARGET_WE_COULD_PREDICT,
        feature=A_FEATURE_THAT_MIGHT_HELP,
        why=WHY_THE_FEATURE_MIGHT_HELP,
        log=LOG,
    )
    # Log the summary string.
    LOG.info(summary_string)

    LOG.info("-------------------------------")
    LOG.info("04. VISUALIZE the selected target and feature.")
    LOG.info("-------------------------------")

    # We required both the target and the feature to be numeric columns.
    # A good way to visualize the relationship
    # between two numeric columns is a scatter plot.

    # Define a path to save the feature vs target scatter plot.
    # REQUIRED: Use the "docs/images" folder to store generated charts.
    CHART_PATH = Path("docs/images/feature-target-scatter.png")

    # Call an imported function that will show a scatter plot
    # Pass in the pandas DataFrame (df) along with the target and feature column names.
    # It will return a matplotlib Axes object representing the scatter plot.
    ax = show_numeric_relationship(
        df, x=A_FEATURE_THAT_MIGHT_HELP, y=A_TARGET_WE_COULD_PREDICT
    )

    # call the save_chart() function and pass in the Axes and the path
    save_chart(ax, CHART_PATH)
    LOG.info(f"Chart saved successfully at {CHART_PATH}.")

    LOG.info(
        "IMPORTANT: Close chart window to continue by clicking its X or close button."
    )
    plt.show()

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
