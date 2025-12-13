# 🎴 FlashcardsDAS – Flashcard Quiz Program

## Description
**FlashcardsDAS** is a Python-based console quiz application that presents users with
 a **random set of seven (7) flashcard questions** from an Excel file.

The user will be asked if he want to play Flashcards.
The user can choose between three categories:
- 🧠 Biology
- 🏝️ Geography
- 📗 History

After completing each quiz, the program displays:
- The user’s **score**
- The **number of questions answered**

The user can then choose to continue with another category or exit the program.


## How It Works
- Questions and answers are stored in an Excel file (FlashcardsDAS.xlsx)
- A separate module (Random_question.py) selects **7 random questions** from the chosen category
- Answers are checked **case-insensitively**
- Scores and progress are displayed after each question


## Program Flow:

  Flashcards Program Flowchart (images/Flashcards_Flowchart.png)


## Repository Structure
FlashcardsDAS/
│
├── images/
│   └── Flashcards_Flowchart.png
├── FlashcardsDAS.py
├── Random_question.py
├── FlashcardsDAS.xlsx
└── README.md



## Excel File Format
The Excel file **FlashcardsDAS.xlsx** contains separate sheets for each category:
- Biology
- Geography
- History1 (name it History1 because in Excel History for sheet name is reserved)

Each sheet must contain **two columns**:

| Questions | Answers |
|----------|---------|
| What is the largest organ in the human body? | skin |
| How many bones does an adult human body have? | 206 |
| Which animal has three hearts? | octopus |

---

## Requirements
- Python **3.8 or higher**
- Required Python libraries:
  - `pandas`
  - `openpyxl`

Install dependencies using:
```bash
pip install pandas openpyxl
openpyxl is required because pandas uses it as an engine to read .xlsx Excel files.

▶ How to Run the Program
Make sure all files are in the same directory.


Run the main program:

python FlashcardsDAS.py

 Example Usage

Are you ready to play the Flashcards quiz? Enter Y or N : Y

Choose a category:
1• Biology
2• Geography
3• History
4• Exit

Choose a category (1-4): 1
You have 7 questions in Biology 🧠

Question 1: What is the largest organ in the human body?
Enter your answer: skin
✅ Correct answer.

Progress: 1/7 | Current Score: 1


⚠️ Error Handling
Invalid category numbers trigger a custom exception (InvalidCategoryError)

Non-numeric input is handled with try/except (ValueError)

Missing Excel file raises a clear error message (FileNotFoundError)



## Random Question Module
The module Random_question.py:

Reads quiz data from FlashcardsDAS.xlsx

Selects 7 random questions using DataFrame.sample()

Displays questions and checks answers

Tracks and displays score and progress

It is called from the main program using:

Rq.rand_ques(sheetname)


👩‍💻👨‍💻 Authors
This program was created by:

Diala Assaf Kourieh

Alexandros Seisoglou

Shaymaa Zaiter

 Purpose
This project was developed for educational purposes, demonstrating:

Modular programming in Python

Random selection of data

Exception handling

User interaction 







