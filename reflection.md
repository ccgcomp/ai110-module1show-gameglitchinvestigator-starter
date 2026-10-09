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

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
