🎴 FlashcardsDAS – Flashcard Quiz Program
Description
FlashcardsDAS is a Python-based console quiz application that presents users with a random set of seven flashcard questions from an Excel file.

The user is first asked whether they want to play the flashcard quiz. If they choose to continue, they can select one of three categories: - Biology - Geography - History

After completing a quiz round, the program displays the user’s score and the number of questions answered. The user can then choose another category or exit the program.

How It Works
Questions and answers are stored in an Excel file named FlashcardsDAS.xlsx. A separate module, Random_question.py, selects seven random questions from the chosen category. Answers are checked case-insensitively, and the current score and progress are shown after each question.

Program Flow
A visual overview of the program logic is provided in the flowchart: images/Flashcards_Flowchart.png

Repository Structure
FlashcardsDAS/
│
├── images/
│   └── Flashcards_Flowchart.png
├── FlashcardsDAS.py
├── Random_question.py
├── FlashcardsDAS.xlsx
├── requirements.txt
└── README.md
Excel File Format
The Excel file FlashcardsDAS.xlsx contains one sheet per category: - Biology - Geography - History1 (named this way because "History" is reserved as a sheet name in Excel)

Each sheet has two columns:

Questions	Answers
What is the largest organ in the human body?	skin
How many bones does an adult human body have?	206
Which animal has three hearts?	octopus
Requirements
Python 3.8 or higher is required.

The program depends on the following Python libraries: - pandas - openpyxl

openpyxl is required because pandas uses it internally to read .xlsx Excel files.

Installing Dependencies (Recommended Method)
Python packages are installed per Python environment, not per IDE. Regardless of whether the program is run from PyCharm, VS Code, or a terminal, dependencies should be installed via Python itself.

All required packages are listed in requirements.txt. To install them, open a terminal in the project directory and run:

python -m pip install -r requirements.txt
If python does not work on your system, try:

python3 -m pip install -r requirements.txt
This ensures that the packages are installed into the same Python environment that runs the program.

How to Run the Program
Make sure all files are located in the same directory. Then run:

python FlashcardsDAS.py
or, if required:

python3 FlashcardsDAS.py
Example Usage
Are you ready to play the Flashcards quiz? Enter Y or N : Y

Choose a category:
1 • Biology
2 • Geography
3 • History
4 • Exit

Choose a category (1–4): 1
You have 7 questions in Biology

Question 1: What is the largest organ in the human body?
Enter your answer: skin
Correct answer.

Progress: 1/7 | Current Score: 1
Error Handling
The program includes basic error handling: - Invalid category numbers trigger a custom InvalidCategoryError - Non-numeric input is handled using try/except (ValueError) - A missing Excel file raises a clear FileNotFoundError

Random Question Module
The module Random_question.py: - Reads quiz data from FlashcardsDAS.xlsx - Selects seven random questions using DataFrame.sample() - Displays questions and checks answers - Tracks and displays score and progress

It is called from the main program using Rq.rand_ques(sheetname).

Authors
This program was created by: - Diala Assaf Kourieh - Alexandros Seisoglou - Shaymaa Zaiter

Purpose
This project was developed for educational purposes to demonstrate modular programming in Python, random data selection, exception handling, and basic user interaction.