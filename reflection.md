# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
--> Actually it looks good at first! I didn't notice anything. The visual looks nice and it gives me hint when I plugged in the numbers.
- List at least two concrete bugs you noticed at the start  
--> I think I started to notice something off when I plugged very high number, like 99, and it still tells me to go higher. Even when I get to 100, it still tells me to go higher, which means that the hint given is broken. Second thing is that when I start a new game, it completely crashes and the game no longer works.
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
--> I used GitHub Copilot and Gemini to help me locate logical errors, refactor my code, and write test cases.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
--> The AI correctly suggested moving my four main game functions out of app.py and into logic_utils.py to separate the logic from the UI. I verified this by running my tests and ensuring the game still loaded perfectly in the browser.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
--> The AI initially suggested I just run the command pytest in the terminal to test my code, which caused a ModuleNotFoundError because of my folder structure. I verified this was wrong by seeing the error, and fixed it by using python3 -m pytest instead.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
--> I knew a bug was officially fixed when my automated tests passed in the terminal and the game behaved correctly when I played it manually in the browser.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
--> I ran a test called test_check_guess_too_high. It showed me that my hint logic was fixed by verifying that if I guessed 75 when the secret was 50, the app correctly returned the "Too High" outcome and the "Go LOWER!" message.
- Did AI help you design or understand any tests? How?
--> Yes, the AI helped me write the pytest functions. It looked at the bugs I had just repaired in logic_utils.py and designed specific scenarios (like checking the Hard mode range) to prove my math was right.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
--> Streamlit reruns the entire Python script from top to bottom every single time a user clicks a button or enters text, meaning it was generating a brand new random number on every interaction.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
--> It is like playing a guessing game with someone who has no short-term memory—every time you guess, they forget the original number unless they write it down in a special notebook. In Streamlit, that "notebook" is called session state.
- What change did you make that finally gave the game a stable secret number?
--> I initialized and saved the secret number inside st.session_state.secret so the app would remember the original generated number across all of those reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
--> I want to keep using the habit of leaving #FIXME comments in my code to mark "crime scenes" before I start changing things. It kept me focused on fixing one bug at a time.
- What is one thing you would do differently next time you work with AI on a coding task?
--> Next time I work with AI, I will be more careful about blindly running terminal commands it suggests, making sure I check what folder I am currently in first.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
--> This project taught me that while AI-generated code might look completely production-ready on the surface, it can still contain hidden logical flaws that require human testing to catch.
