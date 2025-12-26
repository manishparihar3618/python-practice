import os

if (not os.path.exists("MANISHP")):
     os.mkdir("MANISHP")

for i in range(0, 100):
    # os.mkdir(f"MANISHP/Day{i+1}")
    os.rename(f"MANISHP/DAY{i+1}", f"MANISHP/Tutorial{i+1}")
