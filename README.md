# Data Structures Project

This project demonstrates the implementation of various fundamental data structures in Python. It includes the following data structures:

- **Linked List**: A dynamic data structure that allows adding, removing, and displaying elements.
- **Stack**: A Last-In-First-Out (LIFO) data structure with operations such as push, pop, and peek.
- **Queue**: A First-In-First-Out (FIFO) data structure with operations such as enqueue, dequeue, and checking the front element.
- **Binary Tree**: A hierarchical data structure that supports insertion, searching, and tree traversal.

## Features

- Comprehensive implementations of common data structures.
- Modular and reusable code with detailed docstrings and type hints.
- Unit tests for each data structure to ensure correctness and reliability.
- Demonstration of data structure operations through a `main.py` script.
- A `problems` folder containing practical coding problems based on the implemented data structures.
- Continuous Integration (CI) pipeline to ensure code quality and correctness.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-structures-with-python.git
   cd data-structures-with-python
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

To run the application and see the demonstration of the data structures, execute the following command:

```bash
python src/main.py
```

This will showcase the usage of the following data structures:
- Linked List
- Stack
- Queue
- Binary Tree

Each data structure's operations will be demonstrated with sample inputs and outputs.

---

## Problems Folder

The `problems` folder contains coding problems that demonstrate practical use cases of the implemented data structures. Each file in the folder is self-contained and executable, showcasing a specific problem and its solution.

### Running a Problem
To run a specific problem, navigate to the project root directory and execute the file using Python. For example:

```bash
python problems/reverse_linked_list.py
```

This will execute the `reverse_linked_list.py` file and display the expected output for the problem.

---

## Testing and Linting

### Continuous Integration (CI)
This project uses a CI pipeline to ensure code quality and correctness. The pipeline performs the following checks:
1. **Lint Check**: Ensures the code adheres to Python coding standards using `flake8`.
2. **Unit Tests**: Runs all tests in the `tests` folder using `pytest`.

The CI pipeline runs automatically on every push and pull request. If any linting or test fails, the pipeline will fail, and the branch cannot be merged into the `main` branch.

### Checking Locally Before Pushing
To avoid CI failures, you can run the lint check and tests locally before pushing your code:

#### 1. Run Lint Check
```bash
flake8 src tests problems
```
This will check for any linting issues in the `src`, `problems` and `tests` directories.

#### 2. Run All Tests
```bash
pytest
```
This will execute all the test cases defined in the `tests` directory.

#### 3. Running Specific Tests
To run tests for a specific data structure, use:
```bash
pytest tests/test_<data_structure>.py
```
For example:
```bash
pytest tests/test_linked_list.py
```

#### 4. Fix Issues
- Format your files with `black` first.
```bash
black src tests problems
```
- Now, check lint with
```bash
flake8 src tests problems
```
- If the lint check fails, fix the reported issues in your cod individually.
- If any test fails, debug and fix the implementation or the test case.

---

## Directory Structure

```
data-structures-with-python/
├── src/
│   ├── data_structures/
│   │   ├── __init__.py
│   │   ├── linked_list.py
│   │   ├── stack.py
│   │   ├── queue.py
│   │   └── binary_tree.py
│   ├── main.py
├── problems/
│   ├── find_height_binary_tree.py
│   ├── circular_queue.py
│   ├── reverse_linked_list.py
│   ├── ...
│   └── ...
├── tests/
│   ├── test_linked_list.py
│   ├── test_stack.py
│   ├── test_queue.py
│   └── test_binary_tree.py
├── requirements.txt
└── README.md
```

- **src/data_structures/**: Contains the implementation of the data structures.
- **src/main.py**: Demonstrates the usage of the data structures.
- **problems/**: Contains coding problems based on the implemented data structures. Each file is executable and demonstrates a specific problem.
- **tests/**: Contains unit tests for each data structure.
- **.github/workflows/ci.yml**: Defines the CI pipeline for linting and testing.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.