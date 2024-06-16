import base64

# Function to read the Base64 string from a file
def read_base64_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(":: "):
                return line[3:].strip()  # Extract the Base64 string after ":: "

# Function to decode a Base64 encoded string
def decode_base64(encoded_str):
    decoded_data = base64.b64decode(encoded_str)
    try:
        decoded_str = decoded_data.decode('utf-8')  # Try to decode as a UTF-8 string
    except UnicodeDecodeError:
        decoded_str = None  # If it fails, return None for the string part
    return decoded_data, decoded_str

# File path
file_path = '1.txt'  # Replace with the path to your file

# Read and decode the Base64 string
base64_encoded_str = read_base64_from_file(file_path)

if base64_encoded_str:
    decoded_data, decoded_str = decode_base64(base64_encoded_str)
    print("Decoded Data:", decoded_data)
    if decoded_str:
        print("Decoded String:", decoded_str)
    else:
        print("Decoded data is not a valid UTF-8 string.")
else:
    print("No line starting with ':: ' found in the file.")

