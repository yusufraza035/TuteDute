print("==================================================")
print("READ FROM FILE PROGRAM")
print("==================================================")

filename = "sample_data.txt"

with open(filename, 'r') as file:
    content = file.read()

print(f"\nSuccessfully read from '{filename}'")
print(f"File location: {filename}\n")
print("--------------------------------------------------")
print("FILE CONTENT:")
print("--------------------------------------------------")
print(content)
print("--------------------------------------------------")
    
