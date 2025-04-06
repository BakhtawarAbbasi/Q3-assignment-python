# Lesson 11: The Date & Time in Python
# Author: Arif Kasim Rozani - Team Operation Badar

import time
import calendar
from datetime import datetime
import math

# Tick Intervals - Seconds since Epoch (January 1, 1970)
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting Local Time from Ticks
localtime = time.localtime(ticks)
print("\nLocal current time (struct_time):", localtime)

# Getting Formatted Time (e.g., Fri Jan 24 03:41:48 2025)
formatted_time = time.asctime(localtime)
print("\nFormatted local time:", formatted_time)

# Calendar for a Specific Month (January 2025)
print("\nCalendar for January 2025:")
print(calendar.month(2025, 1))

# Using datetime module with strftime()
now = datetime.now()
print("\nCurrent datetime object:", now)
print("Formatted Date & Time:", now.strftime("%A, %d %B %Y, %I:%M:%S %p"))

# Python Math Module Demonstration
print("\n--- Math Module Examples ---")

# Square root and power
print("Square root of 16:", math.sqrt(16))
print("2 to the power of 5:", math.pow(2, 5))

# Value of pi and e
print("Value of pi:", math.pi)
print("Value of e:", math.e)

# Trigonometry
print("Cosine of 0:", math.cos(0))
print("Sine of 90 degrees in radians:", math.sin(math.radians(90)))

# Rounding and absolute value
print("Floor of 5.7:", math.floor(5.7))
print("Ceil of 5.2:", math.ceil(5.2))
print("Absolute value of -10:", math.fabs(-10))

# NaN (Not a Number) Example
nan_value = float('nan')
print("\n--- NaN Example ---")
print("Is nan_value NaN?", math.isnan(nan_value))
print("NaN == NaN:", nan_value == nan_value)  # Always False

# Infinity Example
print("\n--- Infinity Example ---")
print("Positive Infinity:", math.inf)
print("Negative Infinity:", -math.inf)
print("Is Infinity > 1000000?", math.inf > 1_000_000)
print("Infinity minus Infinity:", math.inf - math.inf)  # NaN

# End of Lesson 11
