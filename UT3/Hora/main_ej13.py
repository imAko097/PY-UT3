from hora import Hora

clock = Hora()
clock.show_time()

# 59 seconds
for i in range(59):
    clock.one_second()

clock.show_time()

# 1 second to see if minutes are updated
clock.one_second()
clock.show_time()

# 1 minute to see if hours are updated
for i in range(60):
    clock.one_second()

clock.show_time()

# 1 hour to see if hours are updated
for i in range(3600):
    clock.one_second()

clock.show_time()