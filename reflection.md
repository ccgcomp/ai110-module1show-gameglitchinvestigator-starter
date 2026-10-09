# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game looked normal at first glance — a number-guessing game with a difficulty setting, a hint
toggle, and a "Developer Debug Info" panel showing the secret number, attempts, and score. But once I
started actually playing and comparing the debug info to what the game told me, several things didn't
match up. The hints told me to guess in the wrong direction, the "New Game" button left the game in a
broken, unplayable state instead of cleanly restarting, and the score dropped into negative numbers with
no apparent floor.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 34 (secret was 33, so my guess was higher than the secret) | Hint says "Go LOWER!" | Hint says "Go HIGHER!" | None — no error shown in browser or terminal |
| Clicked "New Game" mid-round | New secret, empty history, attempts reset, guess input usable again | Secret changed, but history persisted from the old round and the guess input became unusable | None — no error shown in browser or terminal |
| 4 wrong guesses in a row on Easy difficulty, no win | Score stays at or floors at 0 after repeated wrong guesses | Score dropped to -20 with no floor | None — no error shown in browser or terminal |
| Guessed 0, then 101, on Normal difficulty (displayed range: 1 to 100) | Guess rejected with an error like "Enter a number between 1 and 100" | Guess accepted; game scored it as a normal guess (hint direction was correct, just shouldn't have been scored at all) | None — no error shown in browser or terminal |
| Guessed 9 (secret was 12) on an even-numbered attempt, Normal difficulty | Outcome "Too Low", hint "Go HIGHER!" since 9 < 12 | Outcome "Too High", hint "Go LOWER!" | None — no error shown in browser or terminal |

---

## 2. How did you use AI as a teammate?

I used Claude in VS Code for this whole thing. A suggestion that worked: adding a bounds check to
`parse_guess` so you can't guess something outside the range, like 0 or 101 on a 1-100 game. I
tested it by just typing those numbers in and watching it get rejected instead of accepted. One I
had to push back on: the first version of that fix added the error message but didn't notice
invalid guesses were still burning an attempt. I only found that by actually playing and trying
bad guesses on purpose, then asked Claude to fix it so attempts only go down on a real guess.
Claude also explained why my "fixed" hints were still wrong sometimes: app.py was converting the
secret to a string on every even attempt, which made the comparison run on text instead of
numbers. So a guess like 9 against a secret of 12 came out "Too High" because the string "9"
alphabetically comes after "1", even though 9 is actually smaller than 12.

---

## 3. Debugging and testing your fixes

I only counted a bug as fixed once it passed pytest AND I retested it live in the app with the
same input that broke it in the first place. Like for the hint bug, I went back and guessed 34 vs
secret 33 again to make sure it said "LOWER" this time. One test, `test_hint_direction_matches_outcome`,
checks the hint message actually matches the outcome instead of being backwards. Claude wrote the
test cases, I ran `pytest -v` myself and read through the output to make sure all 8 passed.

---

## 4. What did you learn about Streamlit and state?

Streamlit basically reruns your whole script from top to bottom every time you click anything. So
a normal variable would just reset every time. `st.session_state` is the workaround. It's a dict
that sticks around between reruns, which is why things like the secret number and score live there
instead of as regular variables.

---

## 5. Looking ahead: your developer habits

Habit I want to keep: actually playing the game after every fix instead of just assuming the code
looks right. That's literally the only reason I caught the attempts bug. Thing I'd do differently:
think about side effects before calling something fixed, instead of stumbling into them after.
This project made me trust AI-written code a lot less by default. It can look done and still be
wrong in a way you only notice by using it.
