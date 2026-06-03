# 🧪 Selenium Pytest Automation Framework
This project is a UI automation framework built using:
- Selenium WebDriver
- Pytest
- WebDriver Manager
- HTML Reporting
- Environment variable support

---

## 📦 Tech Stack

- selenium==4.11.2  
- pytest==7.4.3  
- pytest-html==4.0.0rc7  
- python-dotenv==0.21.0  
- webdriver-manager==4.0.1  

---

API-Automation
 Used openbrewerydb API 
 https://www.openbrewerydb.org/documentation from the list: https://github.com/public-apis/public-apis

## 🚀 Project Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>


How To Run?:

Steps-1
After clonning the project-->Open the project in any IDE like VS code, Pycharm
open cmd/terminal and run below commands to install necesary tools.
pip install selenium==4.11.2 
pip install pytest==7.4.3 
pip install pytest-html==4.0.0rc7 
pip install python-dotenv==0.21.0 
pip install webdriver-manager==4.0.1
pip install requests pytest

open CMD/terminal in IDE---> cd <SportyGroup-Assesement>

copy paste below command in terminal/CMD, this command would run API and functional tests.

pytest -v --html=report.html --self-contained-html

post execution:
checkout report.html for pass fail count.
checkout 'screenshots' folder

# Open Brewery DB API Automation Framework

## Overview

This project contains automated API tests for Open Brewery DB using:

* Python
* Pytest
* Requests

API Documentation:
https://www.openbrewerydb.org/documentation

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests pytest
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

Test Cases
TC_API_001 – Get All Breweries Status Code
Verify breweries endpoint is accessible.
Expected Result: Status code 200.

TC_API_002 – Response Is Not Empty
Verify breweries list contains data.
Expected Result: Response length is greater than 0.

TC_API_003 – Response Is List
Verify API returns a list of breweries.
Expected Result: Response type is list.

TC_API_004 – Required Fields Exist
Verify brewery contains required fields.
Expected Result: id, name, brewery_type, city, and state fields exist.

TC_API_005 – Search Brewery By City
Verify brewery search works for supported cities.
Expected Result: Status code 200 and response data returned.

TC_API_006 – Get Brewery By Valid ID
Verify brewery details can be retrieved using a valid brewery ID.
Expected Result: Status code 200 and returned brewery ID matches requested ID.

TC_API_007 – Get Brewery By Invalid ID
Verify API handles invalid brewery IDs correctly.
Expected Result: Status code 404.

TC_API_008 – Response Time Validation
Verify API responds within acceptable time.
Expected Result: Response time is less than 2 seconds.

## Validation Strategy

### Status Code Validation

Used to confirm that API endpoints are available and responding correctly.

Example:

```python
assert response.status_code == 200
```

---

### Response Structure Validation

Used to ensure the API contract remains stable and returns data in the expected format.

Example:

```python
assert isinstance(response.json(), list)
```

---

### Required Field Validation

Used to verify critical business fields are present in the response payload.

Fields validated:

* id
* name
* brewery_type
* city
* state

Example:

```python
assert "id" in brewery
```

---

### Search Validation

Used to confirm query parameters are applied correctly and valid results are returned.

Example:

```python
response = brewery_api.get_breweries_by_city("san_diego")
```

---

### Resource Retrieval Validation

Used to verify a brewery can be retrieved by a valid brewery identifier.

Example:

```python
assert brewery["id"] == brewery_id
```

---

### Negative Validation

Used to confirm the API handles invalid requests gracefully.

Example:

```python
assert response.status_code == 404
```

---

### Performance Validation

Used as a basic non-functional check to identify significant response-time regressions.

Example:

```python
assert response.elapsed.total_seconds() < 2
```

---

## Framework Structure


api-automation/
│
├── api/
│   └── brewery_api.py
│
├── tests/
│   └── test_brewery_api.py
│
├── conftest.py

```

