print("================================")
print("WRITE TO FILE PROGRAM")
print("================================")
# Define the filename
filename = "sample_data.txt"

# Content to write to the file
content = "Don't forget that gifts often come with costs that go beyond their purchase price. When you purchase a child the latest smartphone, you're also committing to a monthly phone bill. When you purchase the latest gaming system, you're likely not going to be satisfied with the games that come with it for long and want to purchase new titles to play. When you buy gifts it's important to remember that some come with additional costs down the road that can be much more expensive than the initial gift itself."

try:
    with open(filename, 'w') as file:
        file.write(content)
    print(f"\nSuccess! Content written to '{filename}'")
    print(f"File location: {filename}")
    print("\nContent written:")
    print("--------------------------------------------------" )
    print(content)
    print("--------------------------------------------------" )
    
except IOError as e:
    print(f"Error writing to file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
