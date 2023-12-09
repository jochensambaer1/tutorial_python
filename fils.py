import os

def create_blank_md_files(num_files, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_files + 1):
        file_name = f"blank_file_{i}.md"
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, "w") as f:
            f.write("# " + file_name[:-3] + "\n\n")
            f.write("Dit is een leeg Markdown-bestand.\n")

        print(f"Bestand aangemaakt: {file_path}")

if __name__ == "__main__":
    num_files = int(input("Hoeveel lege Markdown-bestanden wil je creëren? "))
    output_dir = input("Geef de naam van de outputmap: ")

    create_blank_md_files(num_files, output_dir)
