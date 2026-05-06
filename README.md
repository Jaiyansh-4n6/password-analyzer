# 🔐 AI-Enhanced Password Strength Analyzer

A smart Python-based password security analyzer that evaluates password strength using **character diversity, randomness detection, sequence analysis, and repetition penalties** to simulate real-world password attack risks.  

Built for learning **Cybersecurity fundamentals**, password auditing, and secure authentication practices.

---

## 🚀 Features

✅ Checks for:
- Uppercase letters  
- Lowercase letters  
- Digits  
- Special symbols  

✅ Intelligent security analysis:
- Sequential pattern detection (`abc`, `123`, `321`)
- Repeated character detection (`aaa`, `111`)
- Randomness/entropy simulation
- Dynamic scoring system
- Real-world crack risk estimation

✅ Gives:
- Final security score
- Security rating
- Personalized improvement suggestions

---

## 📸 Example Output

```bash
### AI-Enhanced Password Strength Analyzer ###

Enter the password : Pass@123

### AI-Enhanced Password Risk Analysis ###

analyzed password : Pass@123
final risk score of the inputted password : 60 / 80
Predicted Real-World Risk : GOOD SECURITY - Estimated to take months to a year to crack.

### Suggestions for Dynamic Defense Improvement ###
--> Avoid simple sequences like '123'
```

---

## 🛠️ Technologies Used

- Python 3
- Python `string` library

---

## 📂 Project Structure

```bash
password-strength-analyzer/
│
├── password_analyzer.py
├── README.md
├── statement.md
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/password-strength-analyzer.git
```

Move into the project directory:

```bash
cd password-analyzer
```

Run the program:

```bash
python project.py
```

---

## 🔍 How It Works

The analyzer performs multiple layers of checks:

1. Detects character diversity
2. Measures password length
3. Simulates entropy/randomness
4. Detects predictable sequences
5. Detects repeated patterns
6. Calculates final risk score
7. Predicts practical cracking difficulty

---

## 📈 Security Ratings

| Score Range | Risk Level |
|---|---|
| 65+ | HIGH SECURITY |
| 50–64 | GOOD SECURITY |
| 35–49 | MEDIUM RISK |
| 20–34 | HIGH RISK |
| Below 20 | CRITICAL RISK |

---

## 🎯 Future Improvements

- GUI version using Tkinter / PyQt
- Password generation feature
