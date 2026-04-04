# 🌑 Basic Day Scoring (BDS)

A minimalist, terminal-based productivity and habit-tracking engine designed to gamify daily disciplines.

## 🧠 What it does

- **Gamified Discipline:** Earn points for every task completed, lose points for every task missed.
- **Dynamic Scheduling:** Assign tasks to specific days of the week (`mo`, `tu`, `we`, `th`, `fr`, `sa`, `su`).
- **Persistence Engine:** Automatically saves your progress, tasks, and total score to `bds_save.json`.
- **Data Integrity:** Includes built-in normalization to validate and repair JSON data structures on startup.


## 🛠️ Commands

| Command | Description |
| :--- | :--- |
| `bds add task` | Add a new task to one or multiple specific days. |
| `bds check task` | Toggle a task's status (Done/Not Done) for today. |
| `bds list task` | List all tasks assigned to the current day. |
| `bds finish` | Score and reset only today's tasks. |
| `bds reset` | Score and reset the entire week's tasks. |
| `bds status` | Display your current cumulative total score. |
| `bds remove task` | Remove a specific task from all assigned days. |
| `bds help` | Show the command menu and current day status. |
| `bds quit` | Safely save and exit the program. |

## 🚀 Requirements

- **Python 3.x**
- No external dependencies (uses standard `json` and `datetime` libraries).

## 📦 Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kayracizmeci/Basic-Day-Scoring.git](https://github.com/kayracizmeci/Basic-Day-Scoring.git)
   cd Basic-Day-Scoring


 
