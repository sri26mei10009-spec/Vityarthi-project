# Vityarthi-project
# Interactive Electricity Bill Calculator

## Overview of the Project
This is a Python program for electricity billing system, applying slab-based pricing and outputting rate in Rs and breakdown of charges.

## Features
* **Interactive Command-Line Interface (CLI):** Provides a clear, continuous menu loop for seamless user navigation and multiple calculations.
* **Auto Calculation:** Automatically distributes consumed units across different pricing slabs and stores the cost of each slab in a list data structure.
* **Error Handling:** Validates all user inputs to catch string inputs or negative numbers, preventing unexpected crashes (`ValueError` handling).
* **Architecture:** Separates the core mathematical logic, menu interface, constants, and validation rules into distinct files within a dedicated `program/` package.
* **Itemized Output:** Displays both the final total cost and a detailed breakdown of charges per billing tier.

## Technologies & Tools Used
* Python 3
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
Open your Command Prompt (cmd), navigate to the folder where you want to save the project, and run the following command:
```cmd
git clone [https://github.com/sri26mei10009-spec/Vityarthi-project.git](https://github.com/sri26mei10009-spec/Vityarthi-project.git)
