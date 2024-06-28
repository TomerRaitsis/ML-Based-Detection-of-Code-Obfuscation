import os

def process_file(input_file):
    settings_dict = {}
    lines_arr = []
    
    with open(input_file, 'r') as file:
        line = file.readline()
        while line:
            line = line.replace('"', '')  # Remove double quotes from the line
            if line.startswith('set'):
                # Extract the key and value
                parts = line.split('=', 1)
                if len(parts) == 2:
                    key = parts[0].split()[1]  # Get the key part (second element after split by space)
                    val = parts[1].strip()  # Get the value part
                    settings_dict[key] = val
            else:
                # Store the line if it ends with ".exe"
                lines_arr.append(line.strip())  # Append stripped line to lines_arr
            
            line = file.readline()

    # Process lines_arr to replace keys with values from settings_dict
    for i in range(len(lines_arr)):
        split_line = [item for item in lines_arr[i].strip().split('%') if item]  # Split each line by '%'
        for j in range(len(split_line)):
            for key, value in settings_dict.items():
                if split_line[j] == key:
                    split_line[j] = value  # Replace key with value

        lines_arr[i] = ''.join(split_line)  # Join split_line into a single string without '%'

    return settings_dict, lines_arr

def compare_extractions(files):
    extractions = {}
    
    for file in files:
        settings, lines = process_file(file)
        extractions[file] = {
            'settings': settings,
            'lines': lines
        }
    
    # Compare settings
    print("Comparing Settings:")
    keys = set()
    for extraction in extractions.values():
        keys.update(extraction['settings'].keys())
    
    for key in keys:
        values = {file: extractions[file]['settings'].get(key, 'Not found') for file in files}
        if len(set(values.values())) > 1:
            print(f"Difference in key '{key}':")
            for file, value in values.items():
                print(f"  {file}: {value}")
    
    # Compare lines
    print("\nComparing Lines:")
    max_lines = max(len(extraction['lines']) for extraction in extractions.values())
    
    for i in range(max_lines):
        line_values = {file: extractions[file]['lines'][i] if i < len(extractions[file]['lines']) else 'Not found' for file in files}
        if len(set(line_values.values())) > 1:
            print(f"Difference in line {i+1}:")
            for file, line in line_values.items():
                print(f"  {file}: {line}")

# List of files to process and compare
input_files = ['file_14.txt', 'file_20.txt', 'file_33.txt']
compare_extractions(input_files)

