import os

def create_md_files_from_txt(txt_dir):
    for txt_file in os.listdir(txt_dir):
        if txt_file.endswith(".txt"):
            txt_path = os.path.join(txt_dir, txt_file)

            with open(txt_path, "r", encoding="utf-8") as txt:
                lines = txt.readlines()

            output_dir = os.path.splitext(txt_file)[0]
            output_dir = output_dir.replace(" ", "_")
            output_dir = os.path.join(txt_dir, output_dir)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for line in lines:
                file_name = line.strip() + ".md"
                file_path = os.path.join(output_dir, file_name)

                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("# " + line.strip() + "\n\n")
                        f.write("Dit is een leeg Markdown-bestand.\n")
                    print(f"Bestand aangemaakt: {file_path}")
                except Exception as e:
                    print(f"Fout bij het maken van bestand: {file_path}")
                    print(f"Foutbericht: {str(e)}")

if __name__ == "__main__":
    txt_dir = input("Geef het pad naar de map met tekstbestanden: ")

    create_md_files_from_txt(txt_dir)
