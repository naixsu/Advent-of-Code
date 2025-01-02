import os
import sys

def create_day_files(day_number):
    directory = f"day_{day_number}"
    os.makedirs(directory, exist_ok=True)
    template_file = "day_x.py"

    if not os.path.isfile(template_file):
        print(f"Error: Template file '{template_file}' does not exist.")
        sys.exit(1)

    with open(template_file, 'r') as f:
        template_code = f.read()

    with open(os.path.join(directory, 'part_1.py'), 'w') as f:
        f.write(template_code)

    with open(os.path.join(directory, 'part_2.py'), 'w') as f:
        f.write(template_code)

    print(f"Generated {directory} with part_1.py and part_2.py")


if len(sys.argv) != 2:
    print("Usage: python gen.py <day_number>")
    sys.exit(1)

day_number = sys.argv[1]
create_day_files(day_number)
