import json

# Function to process the file system data and extract the required values
def extract_filesystem_data(filesystem_info):
    # Split the data into lines and ignore the first line (header)
    lines = filesystem_info.split('\n')[1:]  # Skip the first line (header)
    
    # Extract the relevant fields
    result = []
    for line in lines:
        if line.strip():  # Skip empty lines
            # Split by any whitespace, this will handle spaces and tabs correctly
            parts = line.split()
            if len(parts) == 6:  # Ensure that the line has exactly 6 parts
                size = parts[1]  # The second part is Size
                used = parts[2]  # The third part is Used
                avail = parts[3]  # The fourth part is Avail
                use_percent = parts[4]  # The fifth part is Use%
                mounted_on = parts[5]  # The sixth part is Mounted on
                result.append(f"Mounted on: {mounted_on}, Size: {size}, Used: {used}, Avail: {avail}, Use%: {use_percent}")
    
    return result

# Function to process all hosts
def process_all_hosts(json_data):
    host_data = json_data.get('host', {})
    for ip, data in host_data.items():
        filesystem_info = data[2]
        print(f"Filesystems for IP: {ip}")
        filesystem_values = extract_filesystem_data(filesystem_info)
        for entry in filesystem_values:
            print(entry)
        print()  # Print a blank line between IPs

# Read the input JSON from the file
input_file = 'input.json'

try:
    with open(input_file, 'r') as file:
        input_json = json.load(file)
    
    # Run the script with the loaded JSON data
    process_all_hosts(input_json)

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{input_file}'. Please check the file format.")

