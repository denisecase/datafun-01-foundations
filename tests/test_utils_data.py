"""tests/test_utils_data.py - Tests for reusable data utility functions.

WHY: Professional Python projects include tests to verify that reusable
     functions work correctly and to catch problems early when changes
     are made.

OBS: You do not need to read or modify this file.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging

import pandas as pd

from datafun.utils_data import get_analyst_description, inspect

# === CONFIGURE A LOGGER FOR TESTS ===

LOG: logging.Logger = logging.getLogger("test_utils_data")


# === TEST INSPECT DATA ===


def test_inspect() -> None:
    """Confirm inspect returns useful facts about the data."""

    df: pd.DataFrame = pd.DataFrame(
        {
            "name": ["alpha", "beta"],
            "value": [10, 20],
        }
    )

    overview: str = inspect(
        df=df,
        grain="one observation",
        log=LOG,
    )

    assert "one observation" in overview
    assert "Row count: 2" in overview
    assert "Column count: 2" in overview
    assert "name" in overview
    assert "value" in overview


# === TEST DESCRIPTION ===


def test_get_description() -> None:
    """Confirm get_description returns the analyst's declarations."""

    description: str = get_analyst_description(
        grain="one penguin",
        target="body_mass_g",
        feature="flipper_length_mm",
        why="Larger penguins may have longer flippers.",
        log=LOG,
    )

    assert "one penguin" in description
    assert "body_mass_g" in description
    assert "flipper_length_mm" in description
    assert "Larger penguins may have longer flippers." in description
