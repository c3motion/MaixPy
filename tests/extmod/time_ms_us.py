import utime
try:
    utime.sleep_ms
except AttributeError:
    print("SKIP")
    raise SystemExit

utime.sleep_ms(1)
utime.sleep_us(1)
print(utime.ticks_diff(utime.ticks_ms(), utime.ticks_ms()) <= 1)
print(utime.ticks_diff(utime.ticks_us(), utime.ticks_us()) <= 500)

# ticks_cpu may not be implemented, at least make sure it doesn't decrease
print(utime.ticks_diff(utime.ticks_cpu(), utime.ticks_cpu()) >= 0)
