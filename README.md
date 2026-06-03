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


## 🚀 Project Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>

How To Run?:

Steps-1
--------
After clonning the project-->Open the project in any IDE like VS code, Pycharm
open cmd/terminal and run below commands to install necesary tools.
pip install selenium==4.11.2 
pip install pytest==7.4.3 
pip install pytest-html==4.0.0rc7 
pip install python-dotenv==0.21.0 
pip install webdriver-manager==4.0.1

open command prompt/terminal in any IDE---> cd <SportyGroup-Assesement>

copy paste below command in terminal/CMD, this command would run API and functional tests.

pytest -v --html=report.html --self-contained-html

post execution: 
1. checkout report.html for pass fail count. 
2. checkout 'screenshots' folder

Please check out the attached gif.
![<img width="1370" height="675" alt="Image" src="https://github.com/user-attachments/assets/6b788a58-2bd9-421d-b0d7-afb781a0c64c" />]
