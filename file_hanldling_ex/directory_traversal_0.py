import os

def generate_report(directory):
    report = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]

            if extension not in report:
                report[extension] = []

            report[extension].append(file_path)

    with open(os.path.join(directory, 'report.txt'), 'w') as report_file:
        for extension in sorted(report.keys()):
            report_file.write(f".{extension}\n")
            for file_path in sorted(report[extension]):
                report_file.write(f"- - - {file_path}\n")


directory = input()
generate_report(directory)
print("Report generated successfully.")
