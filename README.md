# Finite Automata Based Password Validator  
### Theory of Automata – Project by Diyorbek Ismoilov (ID: 250487)

---

## 📌 Overview  
This project demonstrates how **Deterministic Finite Automata (DFA)** can be used to formally define and validate password rules. Instead of writing simple if-else checks, we design a DFA that models the password policy and then implement a DFA simulator in Python.

This approach links theoretical automata concepts with practical real-world applications such as authentication systems.

---

## 📌 Problem Statement  
Weak passwords pose major security risks in real systems. A strong password policy must ensure:  

- Minimum length requirement  
- Inclusion of required character types  
- No forbidden characters  
- Fully deterministic validation  

To guarantee correctness, we model the policy using a **Deterministic Finite Automaton (DFA)**.

### **Goal:**  
Build a DFA that validates passwords according to the following rules:

1. **Length ≥ 6**  
2. **At least one uppercase letter (A–Z)**  
3. **At least one digit (0–9)**  
4. **Only letters and digits allowed**  
5. Any forbidden character → transition to a **dead state**

---

## 📌 Automata Model Used

### ✔ Alphabet (Σ)
Σ = { U, L, D }
Where:
U = any uppercase letter
L = any lowercase letter
D = any digit
X = any forbidden symbol → leads to dead state

markdown
Copy code

### ✔ States (Q)  
Each state encodes 3 flags:

- `hasUpper` – whether uppercase seen  
- `hasDigit` – whether digit seen  
- `lenOK` – whether length ≥ 6  

Example states:
- `q0`: no uppercase, no digit, length < 6  
- `qU`: uppercase seen, digit not yet seen  
- `qD`: digit seen, uppercase not seen  
- `qUDLen`: uppercase + digit + length ≥ 6 → **ACCEPTING STATE**  
- `qDead`: forbidden input reached  

### ✔ Transition Rules  
- Reading `U` → set uppercase flag  
- Reading `D` → set digit flag  
- After the 6th symbol → set length flag  
- Reading `X` → go to `qDead`  

### ✔ Accepting States  
Any state in which:
hasUpper = True
hasDigit = True
lenOK = True
