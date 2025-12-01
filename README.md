# Finite Automata Based Password Validator  
### Theory of Automata – Project by Diyorbek Ismoilov (ID: 250487)

---

## 📌 Problem Statement

Weak passwords are a significant security risk in real authentication systems. To ensure strong user credentials, applications must automatically validate passwords according to a clear and enforceable policy.

Instead of validating passwords using scattered conditional statements, this project uses **Deterministic Finite Automata (DFA)** to formally describe the password policy. Using an automaton guarantees that the validation logic is:

- Deterministic  
- Correct  
- Verifiable  
- Easy to simulate and test (using JFLAP)  
- Simple to implement programmatically (Python)

---

## 📌 Password Policy Requirements

A valid password must satisfy **all** of the following:

1. **Length ≥ 6**
2. **At least one uppercase letter (A–Z)**
3. **At least one digit (0–9)**
4. **Only letters and digits are allowed**  
5. Any forbidden character → transition to a **dead state**

This set of rules is modeled as a deterministic finite automaton.

---

## 📌 Automata Model Used (DFA)

### **Alphabet (Σ)**

Σ = { U, L, D }
Where:
U = uppercase letter (A–Z)
L = lowercase letter (a–z)
D = digit (0–9)
X = forbidden symbol → DEAD STATE

### **States (Q)**

Each DFA state represents the progress of 3 conditions:

- `hasUpper`  → Have we seen an uppercase letter?  
- `hasDigit`  → Have we seen a digit?  
- `lenOK`     → Is the length ≥ 6?  

**Example states:**

| State | Meaning |
|-------|---------|
| q0 | No uppercase, no digit, length < 6 |
| qU | Uppercase seen |
| qD | Digit seen |
| qUD | Uppercase + digit seen |
| qLen | Length ≥ 6, but missing uppercase or digit |
| qUDLen | Uppercase + digit + length ≥ 6 → **ACCEPTING STATE** |
| qDead | Forbidden character → trapped forever |

### **Start State**
q0

### **Accepting States**
Any state where:
hasUpper = True
hasDigit = True
lenOK = True

### **Dead State**
qDead → entered if any character ∉ Σ
## ▶️ How to Run the Python Programs

### **1. Running the GUI version (Tkinter)**

Requires Python 3.

```bash
cd code
python password_gui.py
A window will appear where you can enter a password and click Validate.
A pop-up message will show whether the DFA accepts or rejects the password.

2. Running the CLI (Terminal) version
python PROJECT.py
Enter a password in the terminal and see the DFA-based validation result.



Steps
Launch JFLAP

Go to File → Open

Select:


automata/PROJECT.jff
To simulate:

Click Input → Step by Step

Enter a test password

Observe how the DFA transitions through states

If the DFA ends in an accepting state, the password is valid

This allows step-by-step theoretical verification.

📘 Theoretical Notes
Why model password rules with a DFA?
DFA ensures formally correct behavior

No ambiguous conditions

Easy to visualize & debug in JFLAP

Pure deterministic transitions

Perfect match for rule-driven validation systems

Benefits:
Guarantees total rule enforcement

Helps students connect theory → real world

Demonstrates how automata are used in compilers, parsers, and security systems

📌 Conclusion
This project demonstrates how finite automata can be applied to solve a practical, real-world problem: password validation. Using a DFA provides a mathematically sound, deterministic, and verifiable model.

The project includes a complete DFA (.jff), Python implementations (GUI and CLI), and theoretical documentation.

📬 Contact


Author: Diyorbek Ismoilov  
Student ID: 250487
Course: Theory of Automata
