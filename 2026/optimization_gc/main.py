import gc

# threshold values
print(gc.get_threshold())  # (2000, 10, 0)
"""
↑ threshold = ↓ latency + ↓ CPU, но ↑ RAM
"""

# gc.set_threshold(1000, 10, 10)

# gc.collect() # Force start of build

# gc.disable() # Disabling automatic build
