import os
import sys

class Warnings() :
    def __init__(self, id: str, message: str):
        self.id = id
        self.message = message
    def match(self, line: str) -> bool:
        return self.id in line
    def print(self, line_number: int) -> None:
        print(self.message, 
                "See thinpad_top.runs/synth_1/runme.log:{} for more information.".format(line_number))

warnings = []
warnings.append(Warnings("[Synth 8-87]",   "Latch identified."))
warnings.append(Warnings("[Synth 8-327]",  "Latch identified."))
warnings.append(Warnings("[Synth 8-295]",  "Timing loop identified."))
warnings.append(Warnings("[Synth 8-6858]", "Multiple Driven Net identified."))
warnings.append(Warnings("[Synth 8-6859]", "Multiple Driven Net identified."))

# TODO: add more warnings here

try:
    path = os.path.join("thinpad_top.runs", "synth_1", "runme.log")
    f = open(path, "r")
    synth_time = os.path.getmtime(path)
except Exception as e:
    print("Failed to open synthesis log file. Have you synthesized the project before committing?")
    sys.exit(1)

import subprocess
x = subprocess.run(["git", "diff", "--cached", "--name-only"], stdout=subprocess.PIPE)
x = x.stdout.decode("utf-8").split("\n")[:-2]
for p in x:
    if not p.endswith(".v") and not p.endswith(".sv"):
        continue
    t = os.path.getmtime(p)
    if t > synth_time:
        print("Synthesis result is out of date.")
        sys.exit(1)

line_number = 1
flag = False

while True:
    line = f.readline()
    if not line:
        break
    for w in warnings:
        if w.match(line):
            w.print(line_number)
            flag = True
    line_number += 1

if flag:
    sys.exit(1)

sys.exit(0)
