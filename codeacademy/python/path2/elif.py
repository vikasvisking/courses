

def grade_converter(gpa):
  if gpa >= 4.0:
    grade = "A"
    return grade
  elif gpa >= 3.0:
    grade = "B"
    return grade
  elif gpa >= 2.0:
    grade = "C"
    return grade
  elif gpa >= 1.0:
    grade = "D"
    return grade
  else:
    return "F"
  