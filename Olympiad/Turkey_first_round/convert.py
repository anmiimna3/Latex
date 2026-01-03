from hashlib import sha256
import re

for i in range(31, 53):
    with open(f"./answers/{i}.tex", 'r') as f:
        print(i)
        line = f.readlines()[-1]
        line = line.replace("$", "")
        line = line.split("=")[-1].strip()
        with open(f"./coded/{i}.tex", 'w') as g:
            if ("frac" in line):
                nums = re.findall("{.*?}", line)
                g.write("$\\frac{" + sha256(nums[0][1:-1].encode()).hexdigest()[:5] + "}{" + sha256(nums[1][1:-1].encode()).hexdigest()[:5] + "}$")
            else:
                g.write("$" + sha256(line.encode()).hexdigest()[:5] + "$")
