# Vityarthi-project
# Interactive Electricity Bill Calculator

## Overview of the Project
This is a Python program for electricity billing system, applying slab-based pricing and outputting rate in Rs and breakdown of charges.

## Features
* **Interactive Command-Line Interface (CLI):** Provides a clear, continuous menu loop for seamless user navigation and multiple calculations.
* **Auto Calculation:** Automatically distributes consumed units across different pricing slabs and stores the cost of each slab in a list data structure.
* **Error Handling:** Validates all user inputs to catch string inputs or negative numbers, preventing unexpected crashes (`ValueError` handling).
* **Architecture:** Separates the core mathematical logic, menu interface, constants, and validation rules into distinct files within a dedicated `program/` package.
* **Output:** Displays both the final total cost and a detailed breakdown of charges per billing tier.

## Technologies & Tools Used
* Python 3.14.7
* Git / GitHub
* Command Prompt (Windows) or Terminal (Mac/Linux)

---

## Prerequisites & Installation

Before running the project, you need to have Git, Python, and pip installed on your system. 

### 1. Install Git
* Go to the official [Git Downloads page](https://git-scm.com/downloads).
* Download the installer for your operating system and follow the setup wizard.
* To verify the installation, open your Command Prompt (cmd) and type: `git --version`

### 2. Install Python & pip
* Go to the official [Python Downloads page](https://www.python.org/downloads/).
* Download the latest version of Python 3.
* **Important during setup:** Check the box that says **"Add Python to PATH"** at the bottom of the installer before clicking "Install Now".
* *Note: `pip` (Python's package installer) is automatically included with Python 3 installations.*
* To verify, open Command Prompt and type: 
  * `python --version`
  * `pip --version`

---

## Steps to Clone & Run the Project in Command Prompt

Once you have installed the required tools, follow these steps to run the calculator:

**Step 1: Clone the Repository**
Open your Command Prompt (cmd), and run the following command:
```cmd

git clone https://github.com/sri26mei10009-spec/Vityarthi-project.git

```

**Step 2: Navigate to the Project Directory**
Change your current directory to the downloaded repository using the `cd` command:
```
cd Vityarthi-project

```

**Step 3: Run the Application**
Execute the main script using Python:
```
python main.py

```
## Usage Instructions
1. **Start the Application:** Run `python main.py` in your command prompt. The main menu will appear on your screen.
2. **Select an Action:** 
   * Type `1` and press **Enter** to calculate a new electricity bill.
   * Type `2` and press **Enter** to exit the application safely.
3. **Enter Consumption Data:** If you selected `1`, the prompt will ask for the number of units consumed. Type a positive numerical value (e.g., `150` or `125.5`) and press **Enter**.
4. **Review the Bill:** The program will instantly output the calculation, showing a list format of costs for each specific slab alongside the final total amount in Rs.
5. **Continue or Exit:** After displaying the bill, the application automatically returns to the main menu. You can enter new units to calculate another bill or type `2` to quit.

---

## Instructions for Testing
To thoroughly test the application, perform the following actions when the menu appears:

1. **Test valid input (Slab 1):** Select option `1` and enter `90`. The expected total is Rs 450.
2. **Test valid input (Slab 2):** Select option `1` and enter `150`. The expected total is Rs 850 (500 for the first 100 units + 350 for the remaining 50 units).
3. **Test Error Handling:** Select option `1` and type some random letters (e.g., `abc`). The system should display an error and return you to the main menu instead of crashing.
4. **Test Exit:** Select option `2` to verify that the program closes cleanly.
"""
