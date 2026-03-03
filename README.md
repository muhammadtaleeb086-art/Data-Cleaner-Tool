# Data Cleaner Tool

A Python-based Data Cleaning Pipeline designed to clean, process, analyze, and track datasets using a structured multi-phase architecture.
This project was built as a practical data science learning project focusing on real-world data preprocessing workflows.
---

## Project Overview
The Data Cleaner Tool allows users to clean TXT and CSV datasets through an automated pipeline.  
It performs data preprocessing, removes inconsistencies, generates reports, creates visualizations, and stores cleaning history in a database.
The project follows a modular **phase-based pipeline design**, making the system readable, scalable, and easy to maintain.
---

## Features
- TXT file cleaning and processing
- CSV data preprocessing
- Missing value handling
- Duplicate removal
- Outlier detection (IQR Method)
- Automatic cleaned file export
- Summary report generation
- Data visualization
- Cleaning history logging using SQLite database
- Modular pipeline architecture

---

## Project Pipeline (Phases)

### Phase 1 – Input Handling
- Reads TXT and CSV files
- Basic cleaning and validation
- Prepares data for processing

### Phase 2 – Data Processing
- Removes duplicate records
- Handles missing values
- Performs statistical summaries
- Word frequency analysis for TXT files

### Phase 3 – Export System
- Saves cleaned datasets
- Creates organized output files

### Phase 4 – Outlier Handling
- Detects outliers using IQR method
- User decides whether to remove outliers

### Phase 5 – Reporting & Visualization
- Generates cleaning summary report
- Creates visual charts for dataset analysis

### Phase 6 – Cleaning Log System
- Stores cleaning operations in SQLite database
- Maintains dataset cleaning history

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite3

---

## Project Structure


data-cleaner-tool/
│
├── main.py
├── phase1_input.py
├── phase2_processing.py
├── phase3_export.py  
├── phase4_outliers.py
├── phase5_report.py
├── phase5_visualization.py
├── phase6_logging.py
│
├── output/
├── database/
├── requirements.txt
└── README.md

---

## Installation & Setup

### 1. Clone Repository
git clone https://github.com/muhammadtaleeb086-art/Data-Cleaner-Tool.git


### 2. Install Dependencies
pip install -r requirements.txt


### 3. Run the Project
python main.py
---

## Example Outputs
- Cleaned TXT / CSV files
- Summary report
- Data visualizations
- Cleaning history logs stored in database

---

## Learning Objectives

This project demonstrates:

- Data preprocessing workflow
- Modular Python project design
- File handling
- Data analysis using Pandas
- Visualization using Matplotlib & Seaborn
- Database logging with SQLite
- Pipeline-based architecture

---

## Future Improvements
- GUI interface
- Support for Excel files
- Automated scheduling
- Advanced anomaly detection
- Web dashboard integration

---

## Author
Taleeb  
Computer Science Student (Data Science)

---
## License
This project is created for educational and learning purposes.








