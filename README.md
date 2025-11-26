# Limit Practice App 📐

A Streamlit application that helps students practice evaluating limits involving square roots and rational expressions.

## Problem Format

The app generates random limit problems of the form:

```
lim (x→-1) √((x + 1) / (x² + cx + b))
```

where `b` and `c` are integers chosen such that:
- The expression creates a 0/0 indeterminate form at x = -1
- The limit simplifies to 1/a for some integer a

## Features

- **Random Problem Generation**: Each refresh generates a new problem with different coefficients
- **Flexible Input**: Accepts answers as fractions (e.g., "1/3") or decimals (e.g., "0.333")
- **Instant Feedback**: Shows whether the answer is correct or incorrect
- **Step-by-Step Explanation**: Bonus feature showing detailed solution steps
- **Clean UI**: Student-friendly interface with clear problem display

## Prerequisites
1. install a version of python betwee 3.9 and 3.12 
(any version before 3.9 and after 3.12 will not install streamlit packages properly)

## Installation

1. Clone this repository
2. Create a virtual environment
```bash
cd streamlit-limit-practice-app

python3.12 -m venv .venv
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How It Works

### Problem Generation
- Randomly selects an integer `a` (between 2-10)
- Calculates `c = a² + 2` and `b = c - 1`
- This ensures the denominator factors as `(x + 1)(x + a² + 1)`
- The limit simplifies to `1/a`

### Answer Validation
- Parses fractions using Python's `Fraction` class
- Accepts decimal approximations (within 0.0001 tolerance)
- Provides immediate feedback

## Project Structure

```
limit-practice-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Web app framework
- **SymPy**: Symbolic mathematics (for potential extensions)
- **Python Fractions**: For exact fractional arithmetic

## Author

Marcel Tawamba
