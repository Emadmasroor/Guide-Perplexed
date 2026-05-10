import yaml

def generate_guide_yaml():
    # The structure of the Guide: Part: Number of Chapters
    guide_structure = {
        1: 76,
        2: 48,
        3: 54
    }

    # List of translators (using lowercase for the YAML keys)
    translators = [
        "friedlander", 
        "pines", 
        "goodman", 
        "munk", 
        "atay", 
        "tibbon"
    ]

    data = {}

    for part, num_chapters in guide_structure.items():
        part_key = f"part{part}"
        data[part_key] = {}
        
        for ch in range(1, num_chapters + 1):
            ch_key = f"ch{ch}"
            # Initialize with empty strings and the YAML pipe symbol placeholder
            data[part_key][ch_key] = {t: "Placeholder text\n" for t in translators}
	    # data[part_key][ch_key] = {t: "" for t in translators}

    # Write to the translations.yml file
    with open('_data/translations.yml', 'w', encoding='utf-8') as f:
        # We use sort_keys=False to keep the Parts and Chapters in order
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_style='|')

    print("Successfully generated _data/translations.yml with 178 chapters.")

if __name__ == "__main__":
    generate_guide_yaml()
