# Initialize the dictionary and array
settings_dict = {}
lines_arr = []

# Open the file and process it line by line
with open('helloworld.txt', 'r') as file:
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

# Print the modified lines_arr
print("Modified Lines Array:")
for line in lines_arr:
    if len(line) < 100000:
         print(line)

