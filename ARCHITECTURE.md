# QA Automation Framework Architecture

## Project Structure

```
SportyGroup-Assesement/
│
│----Api-automation --->api and tests
├── pages/                    # Page Object Model (POM)
│   ├── __init__.py
│   ├── base_page.py         # Base page class with common methods
│   └── [page_objects].py    # Individual page classes
│
├── tests/                    # Test Scripts
│   ├── __init__.py
│   └── test_*.py            # Test modules using pytest
│
├── utils/                    # Utilities & Helpers
│   ├── __init__.py
│   ├── driver_factory.py    # WebDriver initialization & configuration
│   ├── screenshots.py       # Screenshot capture utilities
│   └── [helpers].py         # Other helper functions
│
├── config/                   # Configuration Files
│   ├── __init__.py
│   └── settings.py          # Environment config, URLs, timeouts
│
├── screenshots/              # Test Artifacts
│   └── [date_time]/         # Organized failure screenshots
│
├── conftest.py              # Pytest fixtures & hooks
└── ARCHITECTURE.md          # This file

```

## File Responsibilities

### **pages/**
- **base_page.py**: Base class containing common Selenium operations (find elements, wait, click, type, etc.) inherited by all page objects
- **[page_objects].py**: Individual page classes representing UI screens (one class per page), using Page Object Model pattern to encapsulate selectors and actions

**Purpose**: Centralize UI element locators and interactions to reduce duplication and improve maintainability

---

### **tests/**
- **test_*.py**: Test modules with test classes and methods using pytest conventions
- Tests import page objects and utilities to create readable, maintainable test scenarios
- Follows AAA pattern: Arrange → Act → Assert

**Purpose**: Contains all test cases, organized by feature or user journey

---

### **utils/**
- **driver_factory.py**: Manages WebDriver creation with Chrome mobile emulation configuration, headless mode, and lifecycle management
- **screenshots.py**: Utility functions for capturing screenshots on failure or specific events
- **[helpers].py**: Common functions like waits, data generators, logging, report building

**Purpose**: Reusable helper functions and utilities shared across tests and pages to avoid code duplication

---

### **config/**
- **settings.py**: Centralized configuration including:
  - Base URLs (dev, staging, prod)
  - Implicit/explicit wait times
  - Browser options (mobile emulation, headless mode)
  - Screenshot paths
  - Any environment-specific settings

**Purpose**: Single source of truth for all configuration parameters, enabling easy environment switching

---

### **screenshots/**
- Stores test failure screenshots with timestamps
- Organized by test run date/time for easy debugging
- Helps identify UI issues and visual regressions
---
### **requirements.txt**
Lists all Python dependencies:
- `selenium`: WebDriver automation
- `pytest`: Test framework
- `pytest-html`: HTML report generation
- `python-dotenv`: Environment variable management

**Purpose**: Dependency management for reproducible environment setup

---

**Purpose**: Keep sensitive/environment-specific data out of code

---

## Key Design Principles

1. **Page Object Model**: All page interactions encapsulated in page classes
2. **DRY (Don't Repeat Yourself)**: Common methods in base_page.py
3. **Separation of Concerns**: Configs, pages, tests, utilities clearly separated
4. **Scalability**: Easy to add new pages, tests, and utilities
5. **Mobile Emulation**: Chrome mobile emulation for mobile testing
6. **Pytest Integration**: Fixtures, hooks, and plugins for robust testing
