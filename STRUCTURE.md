# Project Directory Structure

This document outlines the structure of the REMOTE-LAB-MANAGEMENT-SYSTEM project directory, including descriptions of key files and directories.

## Directory Structure

```
REMOTE-LAB-MANAGEMENT-SYSTEM/
├── src/
│   ├── main.py            # Main application file containing the entry point
│   ├── config.py          # Configuration file for application settings
│   ├── handlers/          # Directory containing request handlers
│   │   ├── __init__.py    # Initializes handlers sub-package
│   │   ├── user_handlers.py# Handles user-related requests
│   │   └── lab_handlers.py # Handles laboratory-related requests
│   └── models/            # Directory containing database models
│       ├── __init__.py    # Initializes models sub-package
│       └── lab_model.py    # Contains the Lab model definition
├── tests/                 # Directory for test cases
│   ├── test_main.py       # Tests for the main application
│   └── test_handlers.py    # Tests for request handlers
├── README.md              # Project overview and instructions
└── requirements.txt       # Dependencies required for the project
```

## File Descriptions

- **src/main.py**: This file is the entry point for the application, containing the main logic to start the service.
- **src/config.py**: This file stores the configuration of the application, such as database connection strings and API keys.
- **src/handlers/**: This directory contains different modules for handling requests, segregated by functionality (e.g., user and laboratory management).
- **src/models/**: This directory includes the data structures for the application's database, defining how data will be stored and organized.
- **tests/**: This directory holds the test cases to ensure the application behaves as expected.
- **README.md**: Provides an overview of the project and instructions on how to set it up and contribute.
- **requirements.txt**: Lists all the necessary libraries and dependencies to run the project.