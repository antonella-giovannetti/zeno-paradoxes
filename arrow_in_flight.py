import time
print("Arrow in flight")
def arrow_flight(d_target):
    pos_arrow = 0
    while pos_arrow < d_target:
        pos_arrow += 1
        print(f"Arrow position = {pos_arrow}")
        time.sleep(1)
arrow_flight(10)


