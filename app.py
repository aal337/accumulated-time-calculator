import js
from datetime import timedelta


def calculate(duration_value, duration_unit, frequency_value, frequency_unit, timespan_value, timespan_unit):
    """
    Calculates the accumulated time for a recurring activity.
    Example: 30 minutes per day over 1 year = 182.5 hours
    """
    try:
        # Convert input values to numbers
        duration_val = float(duration_value)
        frequency_val = float(frequency_value) 
        timespan_val = float(timespan_value)
        
        # Convert all values to seconds for uniform calculation
        def to_seconds(value, unit):
            conversions = {
                'seconds': 1,
                'minutes': 60,
                'hours': 3600,
                'days': 86400,
                'weeks': 604800,
                'months': 2629746,  # Average month (365.25/12 days)
                'years': 31556952   # Average year (365.25 days)
            }
            return value * conversions.get(unit, 1)
        
        # Convert to seconds
        duration_seconds = to_seconds(duration_val, duration_unit)
        frequency_seconds = to_seconds(frequency_val, frequency_unit)
        timespan_seconds = to_seconds(timespan_val, timespan_unit)
        
        # Calculation: (duration per frequency) * timespan
        result_seconds = (duration_seconds / frequency_seconds) * timespan_seconds
        
        return result_seconds
    
    except Exception as e:
        return f"Calculation error: {str(e)}"


def format_result(seconds):
    """Formats the result into a readable form"""
    if isinstance(seconds, str):  # Error case
        return seconds
    
    if seconds < 0:
        return "Negative value - please check your inputs"
    
    # Convert to different units
    minutes = seconds / 60
    hours = seconds / 3600
    days = seconds / 86400
    weeks = seconds / 604800
    months = seconds / 2629746
    years = seconds / 31556952
    
    # Choose the best unit based on size
    if years >= 1:
        return f"{years:.2f} years"
    elif months >= 1:
        return f"{months:.2f} months"
    elif weeks >= 1:
        return f"{weeks:.2f} weeks"
    elif days >= 1:
        return f"{days:.2f} days"
    elif hours >= 1:
        return f"{hours:.2f} hours"
    elif minutes >= 1:
        return f"{minutes:.2f} minutes"
    else:
        return f"{seconds:.2f} seconds"


# Simplified initialization - no event handlers needed
js.document.getElementById("res-num").textContent = "(Please enter values and click Calculate)"