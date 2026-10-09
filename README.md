# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** It's a number guessing game in Streamlit. You pick a difficulty, which sets the range
and how many guesses you get, then try to land on the secret number before you run out of attempts.

**Bugs I found:**
1. Hints were backwards. If you guessed too high it told you to go higher, and too low told you to
   go lower. Happened in both the normal comparison and the fallback branch that kicks in when the
   secret gets converted to a string.
2. You could guess numbers way outside the range, like 0 or 101 on a 1-100 game, and it would just
   accept them like a normal guess.
3. "New Game" doesn't fully reset. The secret changes but the history and guess box get stuck.
   Didn't fix this one, just logged it.
4. Score can go negative with no floor. Also didn't fix, just logged it.

**Fixes I made:**
1. Fixed the hint text so "Too High" actually says go lower and "Too Low" says go higher, in both
   branches. Moved `check_guess` into `logic_utils.py` and added a test for it.
2. Added range checking to `parse_guess` so out-of-range guesses get rejected with an error instead
   of being scored. Also fixed the UI message that said "between 1 and 100" no matter what
   difficulty you picked. While testing this I noticed a rejected guess still used up an attempt,
   so I fixed that too. Attempts only go down on a valid guess now.

## 📸 Demo Walkthrough

1. Picked Normal difficulty (range 1 to 100, 8 attempts).
2. Guessed 50, got "Too Low, Go HIGHER!"
3. Guessed 75, still "Too Low, Go HIGHER!"
4. Guessed 90, now "Too High, Go LOWER!"
5. Guessed 80, still "Too High, Go LOWER!"
6. Guessed 77, back to "Too Low, Go HIGHER!"
7. Guessed 78, got "🎉 Correct!" and won with a final score of 5.

## 🧪 Test Results

```
$ pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\School Work\Principles of Software\Code Path\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 8 items

tests\test_game_logic.py ........                                        [100%]

============================== 8 passed in 0.02s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
