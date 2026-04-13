# Project Instructions

## WEDNESDAY: Complete Workflow Phases 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs
2. Phase 2. **Change Authorship** - update the project to your name and GitHub account
3. Phase 3. **Read & Understand** - review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

**Variables** - naming, typing, and displaying data in Python.

In this project, you will choose meaningful variable names,
assign values of different types, and display the results using formatted strings.

## Learning Objectives

After completing this project, you should be able to:

- Explain what a variable is and why naming matters.
- Declare variables for common Python types: `str`, `int`, `float`, `bool`, and `list[str]`.
- Add type hints to variable declarations.
- Use f-strings to display variable values in formatted output.
- Run and validate a professional Python project using `uv`.

## Example Code

The example file is located in `src/datafun/app_case.py`.

It demonstrates:

- declaring constants using `Final` type hints
- using five common Python types: `str`, `int`, `float`, `bool`, `list[str]`
- formatting output with f-strings
- logging the pipeline process
- organizing code with functions and a `main()` entry point

Make sure you have read and successfully run the example before creating your own version.

## Your Phase 4: Technical Modification Task

Since this is the first module, we'll help you plan the technical modification task.

Using the example as a guide:

1. Copy `src/datafun/app_case.py`.
2. Rename the copy to `src/datafun/app_yourname.py` (all lowercase, no spaces).
3. In your new file, update the module docstring with your name and the current date.
4. Change the values assigned to the existing constants to reflect your own information.
   Keep the same variable names and types.

This phase is mainly about confirming that:

- your copied file runs without errors
- your renamed module runs correctly
- you understand how the file name, module name, and run command connect

## Phase 5: Apply the Skills

In your new file, replace the example constants with five variables of your own choosing.

Choose one of each type:

- A `bool` - a true/false fact about a topic you know well
  (e.g., `is_remote_work`, `has_certification`, `requires_travel`)
- An `int` - a whole number related to your topic
  (e.g., `team_size`, `years_in_field`, `project_count`)
- A `float` - a decimal number related to your topic
  (e.g., `budget_multiplier`, `satisfaction_score`, `avg_hours_per_day`)
- A `str` - a short text value
  (e.g., `department_name`, `primary_language`, `home_city`)
- A `list[str]` - a list of related text values
  (e.g., `tools_used`, `certifications`, `regions_served`)

Then update:

- the `get_summary()` function to display your variables
- the docstring in `main()` to describe what your script does
- the documentation in `docs/` to explain your variable choices

Your logic should remain simple.
You do not need functions beyond `get_summary()` and `main()` in this module.

## What to Look For

- Does your variable name clearly describe the value it holds?
- Is the type hint accurate for the value you assigned?
- Does your f-string output read naturally - like a sentence, not a dump of raw data?
- What happens if you assign the wrong type to a variable? Try it and observe the Pyright warning.
- How does using `Final` signal intent to other developers?

## Optional (Advanced)

If you would like to add a `get_statistics()` function similar to the example,
choose a `list[float]` of measurements related to your topic and compute:
`sum`, `min`, `max`, `mean`, and `stdev` using the `statistics` module.
Display the results using an f-string with two decimal places.
