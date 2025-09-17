# Original/Incorrect Version
def odd_or_even(number):
  if number % 2 = 0:    # Use of an assignment operator ("=") instead of an operation of logical equivalence ("==")
    return "This is an even number."
  else:
    return "This is an odd number."

# Correct Version:
def odd_or_even(number):
  if number % 2 == 0:
    return "This is an even number."
  else:
    return "This is an odd number."
  
