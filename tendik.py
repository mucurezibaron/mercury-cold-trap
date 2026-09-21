# tendik.py
# Prokofiev Crater - Tendik Outpost Thermal Model
# Author: [Your Name], Victoria University Year 1 Sem 1
# Data source: MESSENGER mission, 100K in permanent shadow

# Temperature in permanent shadow (real NASA number)
TEMP_SHADOW = 100  # Kelvin
TEMP_SUN = 700     # Kelvin at rim in full sun

print("=== Tendik Outpost - Sol 87 ===")
print(f"Rim (full sun): {TEMP_SUN}K / {TEMP_SUN - 273.15:.0f}C")
print(f"Floor (permanent shadow): {TEMP_SHADOW}K / {TEMP_SHADOW - 273.15:.1f}C")

# Can we mine?
if TEMP_SHADOW <= 110:
    print("-> Ice stable. Can mine.")
else:
    print("-> Ice sublimates. Abort.")

# For GitHub: this is Day 1, v0.1