def BiM(w,h):
    return w/(h/100)**2

def grade():
    score = float(input("Enter your exam score (0-100): "))
    if score >= 90:
        grade = "A"
    elif score >= 80 and score <90:
        grade = "B"
    elif score >= 70 and score<80:
        grade = "C"
    elif score >= 60 and score <70:
        grade = "D"
    else:
        grade = "F"

    return grade