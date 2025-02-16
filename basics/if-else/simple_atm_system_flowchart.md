# Simple ATM System Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Initialize balance, PIN, and attempts]
    B --> C{Attempts > 0?}
    C -->|Yes| D[Prompt user for PIN]
    D --> E{PIN correct?}
    
    E -->|No| F[Decrease attempts]
    F --> G{Attempts remaining?}
    G -->|Yes| H[Show remaining attempts] --> C
    G -->|No| I[Show "Session Logged Out"] --> Z[End]
    
    E -->|Yes| J[Show options menu]
    J --> K{User choice}
    
    K -->|Balance| L[Display balance] --> M[Exit menu]
    
    K -->|Withdraw| N{Balance > 0?}
    N -->|No| O[Show "Insufficient Balance"] --> M
    N -->|Yes| P[Ask for amount]
    P --> Q{Amount <= Balance?}
    Q -->|Yes| R[Deduct amount & show new balance] --> M
    Q -->|No| S[Show "Insufficient Balance"] --> M
    
    K -->|Invalid| T[Show "Invalid option"] --> J
    
    M --> Z
    
    C -->|No| Z
```

## Explanation

- **Start**: The program begins by initializing the balance, PIN, and the number of attempts.
- **PIN Verification Loop**:
  - Checks if there are remaining attempts.
  - Prompts the user to enter their PIN.
  - If the PIN is incorrect, it decreases the number of attempts and informs the user.
  - If attempts run out, it logs out the session.
- **Options Menu**:
  - If the PIN is correct, the user is presented with options to check the balance or withdraw money.
  - **Balance**: Displays the current balance.
  - **Withdraw**:
    - Checks if the balance is greater than zero.
    - Prompts the user to enter the withdrawal amount.
    - Validates if the withdrawal amount is within the available balance.
    - Deducts the amount and updates the balance if valid.
    - Shows an error message if the balance is insufficient.
  - **Invalid Option**: Handles any invalid menu selections by prompting the user again.
- **End**: The program terminates after completing the desired operations or logging out due to failed attempts.

This flowchart visually represents the logical flow and decision-making process within the simple ATM system.
