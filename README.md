# 🎮 Console Tic-Tac-Toe (Python)

A simple two-player **Tic-Tac-Toe (XO)** game built using Python and playable in the terminal. Players take turns choosing positions on a 3×3 grid to try to get three of their symbols in a row, column, or diagonal.

---

## 📌 Features

- Two-player mode (X and O)
- Detects wins in rows, columns, and diagonals
- Detects tie (no winner)
- Simple console interface

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
    ```

2. **Run the Python file**

   ```bash
   python tic_tac_toe.py
   ```

> 💡 Requires **Python 3.x** to run.

---

## 🎮 How to Play

* Each player chooses a number from **1 to 9** representing a cell in the grid:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

* Player 1 uses **X** and Player 2 uses **O**.
* After each turn, the board is updated.
* The game ends when:

  * A player wins by placing three symbols in a row, column, or diagonal.
  * All spaces are filled without a winner (tie).

---

## 🧠 Game Logic

* The board is stored as a list of 9 strings.
* The game checks for:

  * Win conditions in 8 possible ways (3 rows, 3 columns, 2 diagonals)
  * Tie if all positions are filled with no winner
* Invalid moves (out-of-range or taken cells) are handled.

---

## 🛠 Built With

* Python 3
* Standard input/output (no external libraries)

---

## 👤 **Contact**
Feel free to connect if you have any questions or want to collaborate on similar projects!  
- **Name:** Ali Ebrahim Monir Sakr  
- **Email:** alimonirsakr@gmail.com  
- **LinkedIn:** [Ali Monir Sakr](https://www.linkedin.com/in/ali-monir-sakr)  

---

