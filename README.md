# 🔐 Real Time Password Strength Analyzer

A modern cybersecurity-themed password security analyzer built using **React, FastAPI, and Python** that evaluates password strength in real time using:

- Character diversity analysis
- Entropy estimation
- Sequence detection
- Repetition analysis
- Randomness simulation
- Risk prediction logic

Designed to simulate practical password attack risks and promote secure authentication practices.

---

# 🚀 Features

## ✅ Real-Time Password Analysis
- Live password strength detection
- Dynamic score updates while typing
- Instant security feedback

## ✅ Intelligent Security Checks
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Sequential pattern detection (`abc`, `123`)
- Repeated character detection (`aaa`, `111`)
- Randomness analysis
- Entropy estimation

## ✅ Advanced Security Insights
- Password strength rating
- Estimated crack resistance
- Predicted attack risk level
- Estimated crack time
- Personalized improvement suggestions

## ✅ Modern Cybersecurity UI
- Real-time animated strength bar
- Cybersecurity dashboard interface
- Animated terminal scan effect
- Neon cyber grid background
- Interactive UI cards and animations

---

# 🛠️ Technologies Used

## Frontend
- React
- TypeScript
- Tailwind CSS
- Framer Motion

## Backend
- FastAPI
- Python 3

## Python Libraries
- string

---

# 📂 Project Structure

```bash
password-strength-analyzer/
│
├── backend/
│   ├── analyzer.py
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── index.css
│
├── README.md
├── .gitignore
├── statement.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Jaiyansh12/password-analyzer.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd password-analyzer
```

---

# 🔹 Backend Setup

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend Server

```bash
cd backend
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# 🔹 Frontend Setup

## Install Dependencies

```bash
cd frontend
npm install
```

## Start Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 🔍 How It Works

The analyzer performs multiple layers of password auditing:

1. Detects character diversity
2. Measures password length
3. Calculates entropy estimation
4. Simulates randomness
5. Detects predictable sequences
6. Detects repeated patterns
7. Calculates security score
8. Predicts real-world cracking difficulty
9. Generates security recommendations

---

# 📈 Security Rating System

| Score Range | Strength Level |
|---|---|
| 80–100 | Very Strong |
| 60–79 | Strong |
| 40–59 | Medium |
| 20–39 | Weak |
| Below 20 | Very Weak |

---

# 🧠 Risk Prediction Levels

| Risk Level | Estimated Crack Time |
|---|---|
| Low Risk | Days/Weeks |
| Moderate Risk | Hours/Days |
| High Risk | Minutes/Hours |
| Critical Risk | Seconds/Minutes |

---

# 🎯 Future Improvements

- Artificial Intelligence Integration
- Password generator


---

# 📌 Project Purpose

This project was developed to strengthen understanding of:

- Cybersecurity fundamentals
- Password auditing techniques
- Authentication security
- Frontend-backend integration
- Real-time security analysis systems

---

# 👨‍💻 Author
Jaiyansh Dhaulakhandi
