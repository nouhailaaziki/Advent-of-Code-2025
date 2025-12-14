# Advent of Code 2025 — Solutions

A curated and well-documented collection of solutions for Advent of Code 2025 (Days 1–12). This repository contains clean, idiomatic, and well-tested Python solutions that emphasize correctness, clarity, and algorithmic reasoning.

## Table of contents
- [About](#about)
- [Repository layout](#repository-layout)
- [Languages & requirements](#languages--requirements)
- [Testing & inputs](#testing--inputs)
- [Contributing](#contributing)
- [License & attribution](#license--attribution)
- [Author](#author)
- [Achievement](#achievement)

## About
This repository documents my Advent of Code 2025 solutions, including both Part 1 and Part 2 for each day. Each solution focuses on readability and explaining the approach used. The goal is to serve both as a personal record and a learning resource for others.

## Repository layout
Top-level folders are organized by day:
- day01/
- day02/
- ...
- day12/

Inside each day folder you will typically find:
- part1.py, part2.py (day12 was excluded because the problem contained only one part)
- puzzle_input (the puzzle input used)

## Languages & requirements
- Primary language: Python (3.x recommended)
- Some files compatible with Python 2.
- Recommended: create an isolated virtual environment per project.

## Environment setup
Set up a Python virtual environment and install required packages:

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install shapely
python -m pip install pulp
```

Windows (cmd.exe):
```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install shapely
python -m pip install pulp
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install shapely
python -m pip install pulp
```

Notes:
- Replace `python3` with `python` where appropriate for your system.
- `shapely` and `pulp` are optional third-party packages used by some day's solutions; only install them if you plan to run those solutions.

## Testing & inputs
- Puzzle inputs are included when available. If omitted due to size or privacy, you can provide your own input in the required filename.
- Where applicable, unit tests or example inputs are placed beside the solution to verify correctness against sample cases.

## Contributing
Contributions, improvements, or alternative solutions are welcome. If you submit a change:
- Open a pull request with a clear description of the improvement.
- Keep changes focused (e.g., formatting, bugfix, alternative approach).
- Add tests or examples when introducing new behavior.

## License & attribution
This repository is provided for educational purposes. Puzzle prompts are copyrighted by Advent of Code (https://adventofcode.com); these are my independent solutions.

## Author
- Nouhaila Aziki — solutions, documentation, and maintenance  
- Advent of Code: https://adventofcode.com

## Achievement
![Achievement picture](achievement.png)
