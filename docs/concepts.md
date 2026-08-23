# Concepts

> Key concepts introduced in this module.

<!-- Only the first sentence/paragraph of h3 entries are used for the integrated quiz. -->

## 1. Tabular Data

This project begins with tabular data and adds Python as a way to inspect and work with it.

### Tabular data

Data organized into rows and columns, much like a worksheet in a spreadsheet program such as Excel.

Each column holds one kind of information. Each row records one observation: one item, event, or unit being measured.

### pandas DataFrame

A pandas `DataFrame` is a Python object for working with tabular data.

The DataFrame is where the spreadsheet view of data and programming tools meet.

### Grain

The **grain** describes what a single row represents in a dataset.

In a dataset about penguins, for example, one row represents one penguin.
Identifying the grain is one of the first steps an analyst takes with a new dataset. If the grain is unknown, counts, summaries, and relationships can be misinterpreted.

### Variable (a column)

A **variable** is a column in a dataset that records one characteristic of the observations.

Some variables hold numbers that can be measured or calculated with. Others hold categories, labels, dates, identifiers, or text.
"Variable" also has a programming meaning: a named value in Python code. This entry uses the **data** meaning: a characteristic recorded in a column. The two meanings are related but distinct.
For example, penguin data might include:

- species
- island
- bill length
- flipper length
- body mass

### Data type

A **data type** describes the kind of value stored in a column.

Python and pandas track data types for every column.
How a value is stored is useful information, but an analyst must also consider what the variable represents.
A year, for example, may be stored as an integer even though treating it as an ordinary measured quantity might not make sense.
Common data types include:

- integers for whole numbers
- floating-point numbers for measured quantities
- strings or objects for text and categories
- Boolean values for true or false information
- dates and times

### Shape

The **shape** of a dataset is its number of rows and columns.

A dataset with 344 rows and 7 columns contains 344 observations described by 7 variables.
For example: 344 rows × 7 columns

### Analytical question

An **analytical question** is a question suggested by the variables available in a dataset.

At this stage, the goal is not to answer analytical questions. The goal is to recognize what data is available and **what questions it makes possible**.
For example:
Does flipper length appear to be related to body mass?

## 2. Python: Values and Variables

### Value

A **value** is the actual data held by a variable, such as a number, text, or another Python object.

A variable is the name; the value is its contents.
For example, here, `row_count` is the variable and `100` is the value.

```python
row_count = 100
```

### Variable

A **variable** is a name that refers to a value in a program.

A variable works like a labeled container: the name is the label, and the value is the contents.
Variables make it possible to store data, refer to it by a meaningful name, and reuse it.
A good variable name describes the value it holds.
"Variable" also has a data meaning: a column in a dataset. This entry uses the **programming** meaning: a named value in code.
For example:

```python
row_count: int = 100
```

### Constant

A **constant** is a variable whose value is not meant to change while the program runs.

A constant is comparable to a fixed reference, such as a standard tax rate or a company's official mailing address: defined once and referred to wherever needed, but not altered.
Constants are named in `ALL_CAPS_WITH_UNDERSCORES` and marked with `Final` in their type hint.
For example:

```python
from typing import Final

DATA_FOLDER: Final[str] = "data"
```

### Type hint

A **type hint** is an annotation that states the expected type of a value.

A type hint is similar to labeling a box "fragile - glass."
The label does not change the contents, but it tells others what to expect and lets an inspector catch a mismatch.
We can provide type hints, but tools such as **ty** can also **infer** a type from the value itself.
This means VS Code may **display a type even when no hint is written in the code**.
For example, VS Code may display information such as **msg=** beside a logging call.
That text was not typed into the program; it is information supplied by a development tool.

This can make coding feel complicated at first because many tools are trying to help at the same time.
It is normal to encounter unfamiliar information while learning to work in a professional development environment.

Type hints do not change how the code runs.
They provide information that editors and type-checking tools can use to understand code and flag possible errors.

Explicit hints may be added where they improve clarity, but they are not required on every variable.
For example:

```python
column_name = "temperature"  # type inferred as str

column_name: str = "temperature"  # type stated explicitly
```

### String

A **string** is a sequence of characters representing text.

In Python, strings are enclosed in single or double quotes.
For example:

```python
column_name: str = "temperature"
```

### f-string

An **f-string** is a formatted string that inserts variable values directly into text.

An f-string begins with the letter **f** before the opening quote.
Variable names or expressions go inside curly braces.
For example:

```python
row_count: int = 100
message: str = f"The dataset has {row_count} rows."
```

## 3. Python: Files and Packages

### File

A **file** is a named collection of text or data stored on a computer.

Python source code is stored in files ending in **.py**. One **.py** file typically defines one **module**.
For example:

```text
app.py
```

### Module

A **module** is a Python file containing code that can be run directly or imported by another file.

A module's name is its file name without the **.py** extension.
For example:

```shell
uv run python -m datafun.app
```

This command runs the module named **app** inside the **datafun** package.

### Script

A **script** is a Python file intended to be run so the computer carries out its instructions.

In these projects, a script contains a **main** function and a conditional execution guard that calls **main()** when the file is run directly.
For example:

```text
src/datafun/app.py
```

### Package

A **package** is a folder that groups related Python modules.

In **datafun.app**, the dot separates the package name from the module name.
These projects include a special init file in the package folder.
For example:

```text
src/
  datafun/
    __init__.py
    app.py
```

## 4. Python: Running Code

### Terminal

A **terminal** is a text-based interface for giving instructions to the computer by typing commands.

Where a graphical interface offers buttons, menus, and windows to click, the terminal accepts typed commands.
For example:

```shell
uv run python -m datafun.app
```

### Execute / run

To **execute** or **run** a program means to start it so the computer carries out its instructions.

"Execute" and "run" mean the same thing.
For example, this command runs the `app` module.

```shell
uv run python -m datafun.app
```

### Import

An **import** brings code from another module into the current file so its tools, classes, functions, or constants can be used.

The Python Standard Library includes many useful modules that are available without downloading additional packages. For example, **logging** and **typing** come from the Standard Library.
Other packages, such as pandas and **datafun-toolkit**, are project dependencies.
They are listed in **pyproject.toml** and installed into the project environment by a tool such as **uv**.
For example:

```python
import logging
from typing import Final

from datafun_toolkit.logger import get_logger
import pandas as pd
```

### Logging

**Logging** records messages about what a program is doing while it runs.

A log is comparable to a lab notebook or flight recorder. Entries can include timestamps and severity levels and can be saved to a file.
Logging is preferred over **print** in professional projects because **print** displays a message once, while logging can preserve a useful record of program execution.
Common log levels, from least to most severe, are **DEBUG**, **INFO**, **WARNING**, **ERROR**, and **CRITICAL**.
For example:

```python
LOG.info("Starting main processing.")
LOG.warning("Value is unusually high.")
LOG.error("File not found.")
```

### main function

The **main function** is the starting point for the primary workflow in these project scripts.

It contains the instructions that run when **main** is called.
Recognize **main** as the place where the project's primary sequence of instructions begins.
For example:

```python
def main() -> None:
    summary = get_summary()
    LOG.info(summary)
```

### Conditional execution guard

A **conditional execution guard** calls **main** when a Python file is run directly but not when the file is imported as a module.

This is standard Python practice and commonly appears at the bottom of Python scripts.
For example:

```python
if __name__ == "__main__":
    main()
```

---

[◄ Back to Home](index.md)
