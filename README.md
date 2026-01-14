# Python Crash Course (3rd Edition, 2025)

This repository contains my completed exercises, examples, and projects from **_Python Crash Course (3rd Edition, 2025)_ by Eric Matthes**.  
It serves as both a learning record and a reference for core Python concepts, best practices, and small-to-medium Python projects.

Some parts of the book were slightly outdated by the time of completion, so I **updated code and approaches where necessary** to reflect modern Python versions, libraries, and workflows.

---

## 📘 What This Repository Covers

### Part I – Python Basics

- Variables and simple data types
- Strings, numbers, lists, and tuples
- Conditional statements (`if`, `elif`, `else`)
- Dictionaries
- User input and while loops
- Functions
- Classes and object-oriented programming
- File handling and exceptions
- Testing with pytest (install using `pip install pytest`)

Each chapter includes hands-on exercises and practice scripts demonstrating the core concepts.

---

### Part II – Projects

This section includes complete, multi-file, fully-fledged projects that require additional setup beyond running a single Python script.

Projects cover:

- Alien Invasion Game (dependencies: `pygame`)

```bash
python -m pip install --user pygame
```

Note: At the time of writing, pygame only works upto Python version 3.13.11!

- Data visualization with matplotlib and plotly. (dependencies: `matplotlib`, `plotly`, `pandas`)

```bash
python -m pip install --user matplotlib
python -m pip install --user plotly
python -m pip install --user pandas
python -m pip install --user requests
```

- Working with external libraries (dependencies: `requests`)

```bash
python -m pip install --user requests
```

- Learning Log: A Django Project (dependencies: `django`, `django-bootstrap5`)

```bash
python -m pip install --user django
python -m pip install --user django-bootstrap5
```

---

## 🛠️ Updates & Adjustments Made

- Updated deprecated syntax and APIs
- Adjusted examples to work with **modern Python versions (3.13.11)**
- Improved project structure and readability where applicable
- Minor refactors for clarity and maintainability

---

## 🧑‍💻 Requirements

### General

- **Python 3.10+** (recommended)
- `pip` (comes with Python)

Check your version:

```bash
python --version
```
