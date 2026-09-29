# Project Statement

## Problem Statement
Consumers often lack knowledge in how their electricity bills are calculated, particularly when complex. Manually computing these charges can lead to calculation errors and confusion regarding energy consumption costs.

## Scope of the Project
This project is a command-line application built in Python that automatically calculates a user's electricity bill based on the units they have consumed. It handles exact electric bills pricing, validates user inputs to prevent crashes, and outputs a detailed, exact breakdown of the costs alongside the final total.

## Target Users
* Household Consumers: Individuals looking to cross-check and verify their monthly utility bills.
* Building Managers: Professionals who need a quick tool to estimate meter billing for customers.
* Students/teachers: Individuals studying or teaching basic programming logic, conditionals, and data structures.

## High-Level Features
* Interactive CLI Menu: A continuous loop allowing users to calculate multiple bills or exit safely.
* Tiered Cost Calculation: Distributes consumed units across varying pricing slabs using dynamic `if-elif-else` logic.
* Breakdown: Utilizes List data structures to store and display the exact cost incurred within each billing tier.
* Input Validation: Implements error handling to gracefully catch negative numbers and non-numerical text inputs.
* Modular Codebase: Separates application logic, user interface, and constants into distinct, maintainable files.
