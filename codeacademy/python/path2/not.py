statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if (credits >= 120) and not (gpa >= 2.0):
    return "Your GPA is not high enough to graduate."
  if not(credits >= 120) and not (gpa >= 2.0):
    return "You do not meet either requirement to graduate!"
    
    