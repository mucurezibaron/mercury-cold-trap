sun_hours = 10
power = sun_hours * 100
sun_percent =75
wall_temp = 100 + (sun_percent/100) *600
print(f"Power: {power}W")
print(f"wall_temp at {sun_percent}%: {wall_temp}K")