import csv

input_file = csv.DictReader(open("behaviors.csv"))

passed = 0
failed = 0
broken = 0
skipped = 0
unknown = 0

for row in input_file:
    passed = passed + (int(row["PASSED"]))
    failed = failed + (int(row["FAILED"]))
    broken = broken + (int(row["BROKEN"]))
    skipped = skipped + (int(row["SKIPPED"]))
    unknown = unknown + (int(row["UNKNOWN"]))
    
print("Passed=" + str(passed) + ", Failed=" + str(failed) + ", Skipped=" + str(skipped))
