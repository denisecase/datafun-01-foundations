# Project Instructions (Module 1: Variables and Professional Python)

## WEDNESDAY: Complete Workflow Phases 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs
2. Phase 2. **Change Authorship** - update the project to your name and GitHub account
3. Phase 3. **Read & Understand** - review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Again, follow the instructions above to complete:

1. Phase 4. **Make a Technical Modification** - make a change and verify it still runs
2. Phase 5. **Apply the Skills to a New Problem**

## Phase 4 Suggestions

Make a small technical change that does not break the script.
Choose any one of these (or a different modification as you like):

- Change the value of one constant to reflect something true about you
  (e.g., your field, your city, your years of experience)
- Add a new constant of a type not yet in the example
  (e.g., a `dict[str, int]` mapping skill names to years of experience)
- Change the formatting in `get_summary()` to display values differently
  (e.g., display the list items one per line instead of inline)
- Add a new labeled line to the summary output for one of your constants

Confirm the script still runs successfully after your change.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. Same Structure, Your Domain (Directed)

Replace all five constants in your copy with five of your own choosing,
keeping one of each type: `str`, `int`, `float`, `bool`, `list[str]`.

Steps:

- Choose a topic or domain you know well
  (e.g., your profession, a sport, a hobby, a research area)
- Declare one variable of each type related to your topic
- Use `ALL_CAPS_WITH_UNDERSCORES` for constant names
- Add `Final` to each type hint
- Update `get_summary()` to display your variables with clear labels
- Run the script and confirm output appears in the log

Then:

- Describe the topic you chose and why
- Explain what each variable represents in that context
- Identify which type hint was most natural for your data and why

### Phase 5 Suggestion 2. Add Descriptive Statistics (Original)

Add a `get_statistics()` function for a numeric list related to your topic.

Steps:

- Choose a list of at least five numeric measurements related to your domain
  (e.g., scores, prices, durations, distances, temperatures)
- Declare the list as a `list[float]` constant
- Compute: total, count, minimum, maximum, mean, and standard deviation
- Use the `statistics` module for mean and stdev
- Display the results using an f-string with two decimal places
- Run the script and confirm the statistics appear in the log

Then:

- Describe what the numbers represent
- Identify any values that seem unusual and explain why
- Explain what the standard deviation tells you about your data

## Key Skill Focus

As you work, focus on:

- how to choose clear, descriptive variable names
- how type hints communicate intent without changing behavior
- how `Final` signals that a value should not be reassigned
- how f-strings embed variable values into readable output
- how the `statistics` module provides common descriptive measures

Your goal is to declare meaningful variables and display them clearly.

## Professional Communication

Make sure the title and narrative reflect your work.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub Pages)
- src/ (your renamed script)

Ensure your project clearly demonstrates:

- correct variable declarations with type hints
- a working `get_summary()` function with your variables
- successful script execution with output in the log
