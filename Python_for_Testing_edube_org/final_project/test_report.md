## Test Report – `cart.py` Final Project

### Overview

**Scope**: Static analysis of `cart.py`, summary of refactoring decisions, and review of automated test scenarios in `test_cart.py` (white-box and black-box).  

---

### Static Analysis (Pylint)

**Tool**: `pylint` on `cart.py`  
**Overall score**: **6.99 / 10** 

**Main remaining issues**:

- **Style / formatting**
  - **Trailing whitespace**: multiple lines flagged (`C0303`).
  

**Conclusion**: Functional logic is in place, but there is room for minor style cleanup.

---

### Refactoring Decisions in `cart.py`

**Logging architecture**

- **Centralized logger**:
  - Module-level `logger` created via `logging.getLogger(__name__)` with `DEBUG` level.
  - **`format_loggs()`**: provides a unified log format (`timestamp – level – message`).
  - attached a `StreamHandler` (console) at `DEBUG` level.
  - attached `FileHandler('info.log')` at `INFO` level.
  - attached `FileHandler('errors.log')` at `ERROR` level.
  - These are executed at import time to ensure logging is configured once and consistently.

**Input validation separation**

- **`validate_cart(cart)`**:
  - Ensures every item contains both `'price'` and `'quantity'`.
  - Logs an error with the invalid item and returns `False` on failure; otherwise returns `True`.
- **`validate_discount(discount, min_n=0, max_n=100)`**:
  - Enforces:
    - Discount must be `int`.
    - `min_n ≤ discount ≤ max_n` (0–100 by default).
  - On invalid values, logs an error and returns `False`.
- **`check_float(price, min_n=0, max_n=None)`**:
  - Confirms `price` is a `float` and not less than `min_n`, and optionally not larger than `max_n`.
  - Invalid type or range logs an error and returns `False`.
- **`check_int(quantity, min_n=0, max_n=None)`**:
  - Confirms `quantity` is an `int` and not less than `min_n`, and optionally not larger than `max_n`.
  - Invalid type or range logs an error and returns `False`.

**Business logic – `calculate_total(cart, discount=0)`**

- **Happy path**:
  - Initializes `total = 0`.
  - Validates cart structure with `validate_cart`; returns `0` early if invalid.
  - Iterates items:
    - Uses `check_float(item['price'])` and `check_int(item['quantity'])`.
    - If both checks pass, accumulates `price * quantity` into `total`.
    - If any item fails validation, returns `0` immediately (fail-fast behavior).
- **Discount handling**:
  - If `discount` is non-zero:
    - Validated via `validate_discount`; if invalid, returns `0`.
    - Logs an info message about the applied discount.
    - Applies percentage discount: `total -= total * (discount / 100)`.
- **Final logging**:
  - Logs the final total at `INFO` level.
  - Returns the computed `total`.

**Refactoring intent (inferred)**:

- **Separation of concerns**: Validation helpers (`validate_*`, `check_*`) moved out of `calculate_total` for cleaner and testable logic.
- **Robust error handling**: Systematic logging of all invalid inputs before returning early.
- **Clear discount semantics**: Hard boundaries for discounts (0–100) make behavior predictable and testable.

---

### Test Suite and Outcomes (`test_cart.py`)

**Test style**

- **Simple assert-based tests** (no testing framework import).
- Tests are grouped by scenario in a single file, driven by `calculate_total` from `cart.py`.

**Functional coverage**

- **Valid cart scenarios (white-box)**:
  - **Single valid item**:
    - Cart with `price = 25.0`, `quantity = 10` → **expected total = 250**.
  - **Multiple valid items**:
    - Additional item `price = 5.0`, `quantity = 10` → **expected total = 300**.
- **Missing field scenarios (black-box)**:
  - Cart missing `'price'` key.
  - Cart missing both `'price'` and `'quantity'` keys.
  - Carts where only one item in a multi-item cart is invalid (missing `'price'`):
    - First item invalid, second valid.
    - Second item invalid, first valid.
  - All these are expected to yield **total = 0**, confirming that:
    - `validate_cart` rejects any cart where at least one item lacks required fields.
    - `calculate_total` returns `0` when cart validation fails.
- **Empty and malformed carts**:
  - Completely empty cart (`[]`) → **expected total = 0**.
  - Cart with empty product (`[{}]`): the current test asserts `calculate_total(cart_empty) == 0`, which passes but does not actually use `cart_product_empty`; functionally, a cart with `{}` would also be rejected by `validate_cart`.
- **Edge cases around zero**:
  - `price = 0.0`, `quantity = 10` → **expected total = 0** (0 cost items).
  - `price = 25.0`, `quantity = 0` → **expected total = 0**.
- **Boundary tests for positive values**:
  - Very small positive price:
    - `price = 0.1`, `quantity = 10` → **expected total = 1.0**.
  - Minimal positive quantity:
    - `price = 10.0`, `quantity = 1` → **expected total = 10**.
- **Discount boundary tests**:
  - **1% discount**:
    - Base total 250 → **expected total = 247.5**.
  - **99% discount**:
    - Base total 250 → **expected total = 2.5**.
  - **Out-of-range discounts**:
    - `discount = 101` (> 100) → **expected total = 0**.
    - `discount = -1` (< 0) → **expected total = 0**.
    - Confirms that invalid discounts are rejected and lead to total `0`.
- **Negative values (robustness)**:
  - Negative price (`price = -0.1`) with positive quantity → **expected total = 0**.
  - Negative quantity (`quantity = -1`) with positive price → **expected total = 0**.
  - Confirms that negative values are treated as invalid by `check_float` / `check_int`.

**Overall test outcome (logical assessment)**

- All assertions are consistent with the implemented logic in `cart.py`:
  - Valid data paths produce correct totals.
  - Any structural or value-based invalid input leads to a result of `0` and corresponding logging.
- One minor limitation:
  - The test `cart_product_empty = [{}]` currently asserts `calculate_total(cart_empty) == 0`, so it does not truly exercise the `[{}]` case after refactoring - even though the function would reject it.

---

### Summary

- **Static analysis** shows improved code quality, with remaining issues mostly around trailing whitespace.
- **Refactoring** introduced a clear logging configuration, separated validation helpers, and a robust `calculate_total` function that fails fast on invalid inputs and enforces strict discount rules.
- **Tests** comprehensively cover valid flows, missing fields, empty carts, edge and boundary conditions, and invalid/negative values; logically, the suite aligns with the refactored behavior and supports confidence in the implementation.