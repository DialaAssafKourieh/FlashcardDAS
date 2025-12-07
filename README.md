

# 📘 Flashcard Quiz Program

A Python terminal-based quiz game with random questions from Biology, Geography, and History.

## 📌 Overview

This program allows users to take a quiz consisting of **7 random questions** from a chosen category. The questions are read from an Excel file (`FlashcardsDAS.xlsx`) and selected randomly using the **Random_question** module.

After completing each quiz round, users can choose to continue with a new category or exit the program. The program tracks and displays the user’s score and progress after every question.

---

# 🚀 Features

* Three quiz categories:

  * **Biology**
  * **Geography**
  * **History**
* Randomized set of **7 questions** per round
* Input validation for category selection
* Custom exception handling (`InvalidCategoryError`)
* Real-time progress and scoring
* Reads questions and answers from an Excel file using **pandas**

---

# 📂 Project Structure

```
FlashcardQuiz/
│
├── main_program.py        # Main file handling user interactions
├── Random_question.py     # Module that loads and selects questions
├── FlashcardsDAS.xlsx     # Excel file containing questions per sheet
└── README.md              # Project documentation
```

---

# 🧠 How It Works

### ▶ Main Program (`main_program.py`)

The main file handles:

* Starting the quiz
* Asking the user to choose a category
* Ensuring valid input (Y/N, category numbers)
* Calling `rand_ques()` from `Random_question` module
* Looping until the user chooses to exit

It defines a custom error:

```python
class InvalidCategoryError(Exception):
    pass
```

### ▶ Random_question Module (`Random_question.py`)

This module:

* Loads the Excel sheet based on the chosen category
* Randomly selects **7 unique questions**
* Displays each question and checks the user’s answer
* Tracks the score and displays progress
* Prints the final score at the end

Excel File Requirements:

* Must contain sheets named:

  * `Biology`
  * `Geography`
  * `History1`
* Each sheet must include two columns:

  * **Questions**
  * **Answers**

---

# 📥 Installation

### 1. Install required libraries

```bash
pip install pandas
```

### 2. Ensure the Excel file exists

Place `FlashcardsDAS.xlsx` in the same directory as the program.

---

# ▶ Running the Program

Run the main file:

```bash
python main_program.py
```

### Sample Interaction:

```
Are you ready to play Flash Cards quiz? Press Y or N: Y
Choose a category:
1• Biology
2• Geography
3• History
4• Exit
Choose the category (1-4): 1
You have 7 questions in Biology
```

---

# 📊 Excel File Format Example

Sheet: **Biology**

| Questions                           | Answers               |
| ----------------------------------- | --------------------- |
| What is the powerhouse of the cell? | Mitochondria          |
| DNA stands for?                     | Deoxyribonucleic acid |

---

# 🔧 Troubleshooting

### ❗ Error: "Category must be between 1 and 4!"

Occurs when entering an invalid number during category selection.

### ❗ FileNotFoundError

Ensure `FlashcardsDAS.xlsx` is correctly named and in the program directory.

---

# 📄 License

This project is free to use for educational and personal purposes.

---

If you'd like, I can also:
✅ Format this README in **GitHub style**
✅ Add images or diagrams
✅ Add instructions for packaging it as an executable (.exe)

Just let me know!
