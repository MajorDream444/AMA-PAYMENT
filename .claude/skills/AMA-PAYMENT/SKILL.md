```markdown
# AMA-PAYMENT Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the AMA-PAYMENT Python repository. You'll learn about file organization, import/export styles, commit message habits, and how to write and run tests. These guidelines ensure consistency and maintainability across the codebase.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `payment_processor.py`, `user_manager.py`

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .utils import calculate_fee
    from .models import Payment
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    __all__ = ['PaymentProcessor', 'calculate_fee']
    ```

### Commit Messages
- Freeform style, no strict prefix required.
- Average commit message length: ~27 characters.
  - Example: `fix payment calculation bug`

## Workflows

### Add a New Feature
**Trigger:** When adding new functionality to the codebase  
**Command:** `/add-feature`

1. Create a new Python file using snake_case naming.
2. Implement the feature using relative imports for shared utilities or models.
3. Explicitly define exports with `__all__` if needed.
4. Write or update corresponding test files (see Testing Patterns).
5. Commit changes with a clear, concise message.

### Fix a Bug
**Trigger:** When resolving a bug or issue  
**Command:** `/fix-bug`

1. Locate the relevant file(s) using snake_case naming.
2. Apply the fix, maintaining relative import style.
3. Update or add tests to cover the bug fix.
4. Commit with a descriptive message (e.g., `fix payment rounding issue`).

### Run Tests
**Trigger:** To verify code correctness after changes  
**Command:** `/run-tests`

1. Identify test files (pattern: `*.test.*`).
2. Use the project's preferred test runner (framework unknown; check project docs or use `pytest` as a default).
3. Run all test files and review results.
   - Example:
     ```bash
     pytest
     ```
4. Address any failures before merging.

## Testing Patterns

- Test files follow the pattern: `*.test.*` (e.g., `payment_processor.test.py`).
- Testing framework is not specified; try `pytest` or check project documentation.
- Place tests alongside implementation files or in a dedicated `tests/` directory.
- Example test file:
  ```python
  # payment_processor.test.py

  from .payment_processor import PaymentProcessor

  def test_process_payment():
      processor = PaymentProcessor()
      assert processor.process(100) == "Success"
  ```

## Commands
| Command        | Purpose                                 |
|----------------|-----------------------------------------|
| /add-feature   | Scaffold and implement a new feature    |
| /fix-bug       | Apply and commit a bug fix              |
| /run-tests     | Execute all test files in the project   |
```
