import string

# minimum length set for giving bonus score
min_length = 10

# score weightage
# Reduced individual weights and increased total weight for a finer-grained score
weightage = {
    "length_bonus": 25,
    "upper": 15,
    "lower": 15,
    "digits": 15,
    "characters": 15,
    "randomness_bonus": 15,
    "sequence_penalty": -5,
    "repetition_penalty": -5
}

# ading punctuations/symbols using string library 
characters = string.punctuation

# Helper Functions for Pattern Analysis

def check_sequence(password, seq_length=3):
    """Checks for sequential characters (e.g., 'abc', '345', 'zyx') of a minimum length."""
    password_lower = password.lower()
    
    # Check for sequential letters and digits
    for i in range(len(password) - seq_length + 1):
        segment = password_lower[i:i+seq_length]
        
        # Ascending/Descending Letters
        if segment in string.ascii_lowercase or segment in string.ascii_lowercase[::-1]:
            return True
        
        # Ascending/Descending Digits
        digits = "0123456789"
        if segment in digits or segment in digits[::-1]:
            return True
            
    return False

def check_repetition(password, max_rep=3):
    for i in range(len(password) - max_rep + 1):
        segment = password[i:i+max_rep]
        if all(char == segment[0] for char in segment):
            return True
    return False

# Main Analysis Function 

#create a function for analysing the strength of the password
def analyze(password):
    score = 0
    feedback = []

    found = { 
              "upper": False,
              "lower": False,
              "digits": False,
              "characters": False
              }
    
    # 1. Check for character type presence (Positive Scoring)
    for char in password: 
        if char.isupper(): 
            found["upper"] = True 
        elif char.islower():
            found["lower"] = True
        elif char.isdigit():
            found["digits"] = True
        elif char in characters:
            found["characters"] = True
        
    for char_type, is_present in found.items(): 
        if is_present: 
            score += weightage.get(char_type, 0)
        else:
            if char_type == "upper": 
                feedback.append("add some upper case words (A, B, C)") 
            elif char_type == "lower":
                feedback.append("add some lower case words (a, b, c)")
            elif char_type == "digits":
                feedback.append("add some digits (1, 2, 3)")
            elif char_type == "characters":
                feedback.append(f"add some symbols/characters ({string.punctuation})")

    # 2. Length Bonus
    length = len(password) 
    max_length_score = weightage["length_bonus"]
    
    if length >= min_length:
        score += max_length_score
    elif length > 8:
        score += max_length_score - 5
        feedback.append(f"Length is good, but suggested for more than {min_length} characters for maximum protection.")
    elif length > 6:
        score += max_length_score - 10
        feedback.append(f"Length is okay, but suggested for more than {min_length} characters.")
    else:
        feedback.append(f"Length of password is too small, suggested minimum length = {min_length} ")

    # 3. Randomness Bonus (Simulating Entropy)
    unique_chars = len(set(password))
    if unique_chars >= length * 0.75 and length >= 8: # If 75% or more of characters are unique
        score += weightage["randomness_bonus"]
    
    # 4. Pattern/Sequence Penalties (AI-like Risk Analysis)
    if check_sequence(password):
        score += weightage["sequence_penalty"] # penalty is negative
        feedback.append("Avoid simple sequences like 'abc', '123', or '321'. These are easy to guess.")

    if check_repetition(password):
        score += weightage["repetition_penalty"] # penalty is negative
        feedback.append("Avoid repeating characters like 'aaa' or '111'.")

    entropy = round(len(password) * 4.2)

    return score, feedback, entropy

# create a function for counting the resultant rating of the password using if else statements
def rate(score):

    if score >= 80:
        return {
            "strength": "Very Strong",
            "risk": "Low Risk",
            "crack_time": "Years",
            "crack_resistance": "Excellent"
        }

    elif score >= 60:
        return {
            "strength": "Strong",
            "risk": "Moderate Risk",
            "crack_time": "Months",
            "crack_resistance": "Strong"
        }

    elif score >= 40:
        return {
            "strength": "Medium",
            "risk": "Moderate Risk",
            "crack_time": "Weeks",
            "crack_resistance": "Moderate"
        }

    elif score >= 20:
        return {
            "strength": "Weak",
            "risk": "High Risk",
            "crack_time": "Hours",
            "crack_resistance": "Weak"
        }

    else:
        return {
            "strength": "Very Weak",
            "risk": "Critical Risk",
            "crack_time": "Minutes",
            "crack_resistance": "Very Weak"
        }

# create a function to display the final results
def result(password, score, feedback):
    rating_string = rate(score)
    max_possible_score = sum(val for key, val in weightage.items() if not key.endswith('_penalty'))
    
    print("\n\n### AI-Enhanced Password Risk Analysis ###")
    print(f"analyzed password : {password}")
    print(f"final risk score of the inputted password : {score} / {max_possible_score} (Penalties Applied)")
    print(f"Predicted Real-World Risk : {rating_string}")

    if feedback:
        print("\n### Suggestions for Dynamic Defense Improvement ###")
        for suggestion in feedback:
            print(f"--> {suggestion}")
    else:
        print("\nFeedback : Great work! Your password shows high randomness and avoids common patterns, indicating a low real-world risk.")

# create a function to take password from user and display the results ( main program)
def main():
    print("### AI-Enhanced Password Strength Analyzer ###")
    password = input("Enter the password :")

    if not password: 
        print("Password cannot be empty")
        return
    
    final_score, suggestions = analyze(password)
    result(password, final_score, suggestions)

if __name__ == "__main__":
    main()