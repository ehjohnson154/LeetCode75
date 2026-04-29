# Copilot Instructions for LeetCode75

This repository contains isolated LeetCode-style Python problem solutions organized by numbered folders.

## What matters
- Each problem lives in its own top-level folder, e.g. `1_MergeStringAlternately/` and `2_GreatestCommonDivisorInStrings/`.
- Each implementation file defines a `Solution` class with a single public method matching the LeetCode problem signature.
- The repo has no centralized build system, package management, or CI configuration.

## Project conventions
- Keep changes confined to the relevant problem folder.
- Preserve the public `Solution` class and method signature exactly as the problem expects.
- Do not add unrelated infrastructure files, dependencies, or package layouts.
- Treat folders as script-level problem modules rather than importable Python packages.

## Existing patterns
- `1_MergeStringAlternately/mergestringalternately.py` contains the merge algorithm implementation.
- `1_MergeStringAlternately/testingmergestringalternately.py` demonstrates the local `unittest` test pattern.
- `2_GreatestCommonDivisorInStrings/greatestcommondivisorinstrings.py` is another standalone solution file.

## Debugging and validation
- Validate locally by running the relevant Python file directly with standard Python 3.
- Run unit tests using `python -m unittest` against the test file in the same folder, for example:
  - `python -m unittest 1_MergeStringAlternately.testingmergestringalternately`
- Do not assume environment-specific tooling or package installation is required.

## When adding or updating problems
- Follow the existing naming convention: numbered folder + CamelCase problem name.
- Do not invent project-specific build steps or package dependencies that are not present.
- If asked to extend the project, confirm whether the user wants a test file or additional problem directories.