# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  -It looked like a game that where I had to guess a number the system secretly had. I had a limited amount of attempts, but the system would help me with hints. Also, the range of potential answers and number of attempts changed for each difficulty. Wrong answers removed from my score while right answers added to the score. Also, a new round can be started with the "New Game" button.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  -I noticed the hints were backwards so when the answer was lower than my guess, it said to go higher, and when the answer was higher, it said to go lower. It should be the opposite that is happening.
  -I could only play one round of the guessing game, so I would guess correctly or finish the attempts, but even if I clicked "New Game", I couldn't make any more guesses. The button should allow me to make more guesses.
  -Numbers outside of the range were used as the secret answer (had "-25"). The system should only allow secret answers within the given range.
  -Changing the difficulty did not change the secret answer and would still have numbers outside of the range. The range should change for each difficulty so if I had a secret answer of 50 and changed to easy mode, it should lower the secret answer to within that range.
  -The metadata seemed to update an iteration too late. For example, for my first guess, the history, attempts, score, etc. would not change until I guessed a second time. This metadata should be updated right as I make my guess.
  -Score doesn't update correctly. It seems that it should decrease by 5 if wrong, and increase by 5 if correct. However, it seems very inconsistent. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 
 -I used Copilot for this assignment.

- Give one example of an AI suggestion that was correct (including what the AI 
suggested and how you verified the result).

 -I asked the AI to help me find the issue to why I couldn't play any more rounds and explained in detail. The AI was able to find the issue immediately without my help and just what I viewed as a problem. It understood what I wanted fix and found the problem (the game status wasn't being updated to "playing" when there was a new game). It also suggest a solution of updating the game status and other metadata. I was able to verify this by first looking over the code, then running the app again to see if the function now worked, which it did.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

 -So, I only asked about how the score was being updated inconsistently, and the AI suggested a large amount of fixes for a small problem. It suggested to create a new file for the app, updating the logic_utils.py file, and deleting the old app file. Although I had asked for a single fix, it tried doing other fixes that I didn't ask for it to fix such as refactoring. It led to having a string type issue that the app did not have before.I verified this by running the app and doing guesses (which caused the error).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  -I decided if a bug was really fixed with three checks: my own knowledge of reading the code and deciding if it looked good, the tests that existed, and then running the app and trying out different functions to check if anything broke or it was functioning like it was supposed to.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  -One of the tests actually helped me notice specific issue: lexicographical comparison is the not the same as numerical comparison. My code turned the guess into a string, but even if the number was smaller than the secret number, the lexicographical comparison of strings can lead to smaller number being viewed as the greater number. This test was able to identify this problem and help me make the code less buggy.

- Did AI help you design or understand any tests? How?

  -Yes, it did! Every time changes were made, the AI would explain where the code changed, why it changed, and the expected results of the fixes. This gave me the idea of what to expect when verifying the fixes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

-Streamlit's session state acts like a python dictionary that holds important values that is used in the app. This values are kept even through reruns. Streamlit reruns are re-executions of the script that could reinitialize values, which happens when you interact with a button in the app or you explictly call st.rerun(). So, it can restart a game you were playing or a main function.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
  Next time, I think I want to write the line numbers of where fixes should be made, and then try to see where the AI identifies the issues. I can then compare, which could help check the AI or learn more if I was wrong with my placement.

- What is one thing you would do differently next time you work with AI on a coding task?

-I want to be careful with the AI changing the code. I need to analyze what it changed better. I noticed a few problems after keeping the changes. Once you keep the changes, you can't undo it. You can only undo the changes when you have the option of "Keep or Undo", but once you click on "Keep", there is no going back. You need to hope that the AI remembers ALL its changes and you can ask it to go back to the original code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

 -It made me more skeptical of the code generated becase you can't trust code even more than 90% of the time. You always need to check for any mistakes and make sure the logic fits what is trying to be done. 
