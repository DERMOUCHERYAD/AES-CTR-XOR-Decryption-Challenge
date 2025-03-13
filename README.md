# AES-CTR XOR Decryption & Building Power Solver Challenge

## Files Included

- **challenge.py**  
  Contains the original challenge code that encrypts two messages using AES in CTR mode with an additional XOR mask.

- **output.txt**  
  This file contains the encrypted output:
  - The first line corresponds to the test message (with known plaintext).
  - The second line contains the encrypted secret flag.

- **script.py**  
  Your solver script that:
  - Extracts the timestamp from each line.
  - Computes the XOR mask from the timestamp.
  - Recovers the AES-CTR keystream using the known test message.
  - Uses the keystream to decrypt the secret flag from the second line.

- **3good-all.txt**  
  After obtaining the flag, it was stored inside a “box.” This file contains a matrix representing an `input.txt` file. You are expected to feed this input to your solver according to the challenge rules (see below).

- **flagRes.txt**
   the solution after using the solver 

## What Is the Challenge?

Imagine you have a small budget and need to power a set of buildings over many rounds (turns). In each round, you are given:
- A minimum number of buildings that must be powered (to get any profit).
- A maximum limit on the number of buildings that count for profit.
- A profit value for every building you successfully power.

You can purchase various energy resources, each with its own cost, operating expense, lifespan, and sometimes special effects. Your goal is to make strategic decisions about which resources to buy and when—ensuring you always meet the minimum requirements, maximize your profit, and never run out of money.

### The Solver

- **Reads the Game Data:**  
  It takes an input file (here, the matrix in `file.txt` represents the actual `input.txt`).

- **Simulates Each Turn:**  
  For every turn, the solver checks if the buildings powered meet the required minimum, purchases resources if necessary (based on cost-effectiveness), calculates profits, and updates the budget.

- **Produces a Purchase Plan:**  
  The program outputs a schedule that details what resources to buy and when.

> **Note:** The full detailed description of this challenge will be provided later in another repository.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DERMOUCHERYAD/AES-CTR-XOR-Decryption-Challenge.git
   cd AES-CTR-XOR-Decryption-Challenge
    ```

2.  **Install Dependencies:**

Make sure you have Python 3 installed. Then, install the required package:
   ```bash
  pip install pycryptodome
   ``` 

3.  **Run the Challenge Script:**

     - First, you can run challenge.py to understand the encryption process and see how output.txt was generated.
4.   **Solve the Decryption Challenge:**
     - Execute script.py to recover the flag:
        ```bash
       python3 script.py
         ```
5.  **Use the Flag for the Next Puzzle:**
Once you have the flag, open file.txt (which contains a matrix representing an input.txt file). Use your own solver (or modify script.py) to process this input according to the challenge rules and capture the final flag.
  
