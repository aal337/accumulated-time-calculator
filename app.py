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
                'years': 31556952,   # Average year (365.25 days)
                'decades': 315569520  # 10 years
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
    """Formats the result into a readable form with multiple units for decimal places"""
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
    decades = seconds / 315569520
    
    # Function to format multiple units
    def format_multiple_units(total_seconds):
        result_parts = []
        remaining = total_seconds
        
        # Decades
        if remaining >= 315569520:
            decade_count = int(remaining // 315569520)
            result_parts.append(f"{decade_count} decade{'s' if decade_count != 1 else ''}")
            remaining %= 315569520
        
        # Years
        if remaining >= 31556952:
            year_count = int(remaining // 31556952)
            result_parts.append(f"{year_count} year{'s' if year_count != 1 else ''}")
            remaining %= 31556952
        
        # Months
        if remaining >= 2629746:
            month_count = int(remaining // 2629746)
            result_parts.append(f"{month_count} month{'s' if month_count != 1 else ''}")
            remaining %= 2629746
        
        # Weeks
        if remaining >= 604800:
            week_count = int(remaining // 604800)
            result_parts.append(f"{week_count} week{'s' if week_count != 1 else ''}")
            remaining %= 604800
        
        # Days
        if remaining >= 86400:
            day_count = int(remaining // 86400)
            result_parts.append(f"{day_count} day{'s' if day_count != 1 else ''}")
            remaining %= 86400
        
        # Hours
        if remaining >= 3600:
            hour_count = int(remaining // 3600)
            result_parts.append(f"{hour_count} hour{'s' if hour_count != 1 else ''}")
            remaining %= 3600
        
        # Minutes
        if remaining >= 60:
            minute_count = int(remaining // 60)
            result_parts.append(f"{minute_count} minute{'s' if minute_count != 1 else ''}")
            remaining %= 60
        
        # Seconds (if any remaining)
        if remaining > 0 or not result_parts:
            if remaining == int(remaining):
                second_count = int(remaining)
                result_parts.append(f"{second_count} second{'s' if second_count != 1 else ''}")
            else:
                result_parts.append(f"{remaining:.1f} seconds")
        
        return result_parts
    
    # Choose the best format based on size and precision
    if decades >= 1:
        # Check if there are decimal places worth showing
        if decades != int(decades) and decades < 10:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:3])  # Show up to 3 units
        else:
            return f"{decades:.2f} decades"
    elif years >= 1:
        if years != int(years) and years < 10:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:3])
        else:
            return f"{years:.2f} years"
    elif months >= 1:
        if months != int(months) and months < 12:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:2])
        else:
            return f"{months:.2f} months"
    elif weeks >= 1:
        if weeks != int(weeks) and weeks < 8:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:2])
        else:
            return f"{weeks:.2f} weeks"
    elif days >= 1:
        if days != int(days) and days < 14:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:2])
        else:
            return f"{days:.2f} days"
    elif hours >= 1:
        if hours != int(hours) and hours < 48:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:2])
        else:
            return f"{hours:.2f} hours"
    elif minutes >= 1:
        if minutes != int(minutes) and minutes < 120:
            parts = format_multiple_units(seconds)
            return ", ".join(parts[:2])
        else:
            return f"{minutes:.2f} minutes"
    else:
        return f"{seconds:.2f} seconds"


# Simplified initialization - no event handlers needed
js.document.getElementById("res-num").textContent = "(Please enter values and click Calculate)"