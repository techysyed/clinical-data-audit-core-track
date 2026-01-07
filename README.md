# clinical-data-audit-core-track
Core Track solution for Python Winter Sprint 2026 – Clinical Data Audit System

## Overview
This project is part of the **Python Winter Sprint 2026 – Core Track**.
It implements a simple clinical data audit system using Python functions and recursion.

The program validates patient age, collects multiple heart rate readings, raises flags for invalid inputs, raises warnings for abnormal values, and determines a final audit status.

---

## Features
- Age validation (numeric and range-based)
- Recursive input of multiple heart rate readings
- Flag generation for invalid data
- Warning generation for high heart rate values
- Final audit status classification:
  - PASS
  - REVIEW
  - FAIL

---

## Audit Logic
- Age must be between 0 and 120
- Heart rate must be numeric
- Any heart rate greater than 180 bpm raises a warning
- Any invalid input raises a flag

### Final Status Rules
- **FAIL** → Any flag present
- **REVIEW** → No flags, but warnings present
- **PASS** → Clean data (no flags, no warnings)
