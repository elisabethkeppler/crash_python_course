# Rational Class

## Description

This module defines a `Rational` class to represent rational numbers in simplified form using continued fractions for approximation and with precision control.

### Features

- Internal simplification using prime factor decomposition (based on Exercise 3.5).
- Precision-aware approximation using continued fractions.
- Overloads:
  - Arithmetic operators (`+`, `-`, `*`, `/`)
  - Comparison operators (`==`, `<`, `<=`, `>`, `>=`)
  - Casting to `float` and `int`
  - `__str__` and `__repr__` for friendly output
- Optional rounding methods: `to_integer_low()` and `to_integer_upp()`