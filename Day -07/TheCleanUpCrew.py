# write a try/except block that divides two numbers. Add a finally block that prints"Execution complete"
# regardless of whether the division is succeeded or failed.

try:
    print(f"Division is: {2/3:.2f}")

except ZeroDivisionError:
    print("Cannot divide by zero.")
    
finally:
    print("Execution complete.")