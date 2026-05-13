import string

# minimum length set for giving bonus score
min_length = 12

# score weightage
# Reduced individual weights and increased total weight for a final-gained score
weightage = {
    "length_bonus": 19,
    "upper": 19,
    "lower": 19,
    "digits": 19,
    "characters": 19,
    "randomness_bonus": 5,
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


# create a function for counting the resultant rating of the password using if else statements
def rate(score):

    if score >= 80:
        return {
            "strength": "Very Strong",
            "risk": "Low Risk",
            "crack_time": "Many weeks ",
            "crack_resistance": "Excellent"
        }

    elif score >= 60:
        return {
            "strength": "Strong",
            "risk": "Moderate Risk",
            "crack_time": "Days/Weeks",
            "crack_resistance": "Strong"
        }

    elif score >= 40:
        return {
            "strength": "Medium",
            "risk": "Moderate Risk",
            "crack_time": "Hours/Days",
            "crack_resistance": "Moderate"
        }

    elif score >= 20:
        return {
            "strength": "Weak",
            "risk": "High Risk",
            "crack_time": "Minutes/Hours",
            "crack_resistance": "Weak"
        }

    else:
        return {
            "strength": "Very Weak",
            "risk": "Critical Risk",
            "crack_time": "Seconds/Minutes",
            "crack_resistance": "Very Weak"
        }


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

        if char.islower():
            found["lower"] = True

        if char.isdigit():
            found["digits"] = True

        if char in characters:
            found["characters"] = True
        
    for char_type, is_present in found.items(): 

        if is_present: 

            score += weightage.get(char_type, 0)

        else:

            if char_type == "upper": 

                feedback.append("Add uppercase letters (A-Z)") 

            elif char_type == "lower":

                feedback.append("Add lowercase letters (a-z)")

            elif char_type == "digits":

                feedback.append("Add numbers (0-9)")

            elif char_type == "characters":

                feedback.append("Add symbols (!@#$)")

    # 2. Length Bonus
    length = len(password) 

    max_length_score = weightage["length_bonus"]
    
    if length >= min_length:

        score += max_length_score

    elif length > 10:

        score += max_length_score - 5

        feedback.append(f"Use more than {min_length} characters for better security.")

    elif length > 8:

        score += max_length_score - 10

        feedback.append(f"Password should be longer than {min_length} characters.")

    else:

        feedback.append(f"Password too short. Minimum suggested length = {min_length}")

    # 3. Randomness Bonus (Simulating Entropy)
    unique_chars = len(set(password))

    if unique_chars >= length * 0.6 and length >= 8:

        score += weightage["randomness_bonus"]
    
    # 4. Pattern/Sequence Penalties (AI-like Risk Analysis)
    if check_sequence(password):

        score += weightage["sequence_penalty"]

        feedback.append("Avoid sequences like abc or 123.")

    if check_repetition(password):

        score += weightage["repetition_penalty"]

        feedback.append("Avoid repeated characters like aaa or 111.")

    charset_size = 0

    if found["lower"]:
        charset_size += 26

    if found["upper"]:
        charset_size += 26

    if found["digits"]:
        charset_size += 10

    if found["characters"]:
        charset_size += len(characters)

    entropy = round(length * (charset_size ** 0.5))

    # limiting score between 0 and 100
    score = max(0, min(score, 100))

    # getting rating details
    rating = rate(score)

    return {
        "score": score,
        "strength": rating["strength"],
        "risk": rating["risk"],
        "crack_time": rating["crack_time"],
        "crack_resistance": rating["crack_resistance"],
        "entropy": entropy,
        "findings": feedback
    }


# create a function to display the final results
def result(password, analysis):

    max_possible_score = sum(
        val for key, val in weightage.items()
        if not key.endswith('_penalty')
    )
    
    print("\n\n### AI-Enhanced Password Risk Analysis ###")

    print(f"analyzed password : {password}")

    print(f"final risk score of the inputted password : {analysis['score']} / {max_possible_score} (Penalties Applied)")

    print(f"Password Strength : {analysis['strength']}")

    print(f"Predicted Real-World Risk : {analysis['risk']}")

    print(f"Estimated Crack Time : {analysis['crack_time']}")

    print(f"Crack Resistance : {analysis['crack_resistance']}")

    print(f"Estimated Entropy : {analysis['entropy']} bits")

    if analysis["findings"]:

        print("\n### Suggestions for Dynamic Defense Improvement ###")

        for suggestion in analysis["findings"]:

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
    
    analysis = analyze(password)

    result(password, analysis)


if __name__ == "__main__":
    main()