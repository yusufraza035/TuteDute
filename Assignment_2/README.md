# Python Programming Assignment - Complete Solutions

## Assignment Overview
This assignment consists of 4 Python programs demonstrating fundamental programming concepts:
1. **Grade Checker** - Using if-else statements
2. **Student Grades Manager** - Using dictionaries and if-else statements
3. **Write to a File** - Using file operations (write mode)
4. **Read from a File** - Using file operations (read mode)

---

## Program 1: Grade Checker

### Description
A program that takes a numerical score as input and returns the corresponding letter grade based on predefined ranges.

### Grade Scale
- 90+ : "A"
- 80-89 : "B"
- 70-79 : "C"
- 60-69 : "D"
- Below 60 : "F"


### Example Execution

**Input:** 95
**Output:** Grade A

**Input:** 75
**Output:** Grade C

---

## Program 2: Student Grades Manager

### Description
A dictionary-based program that stores student names as keys and grades as values. Allows users to:
- Add new students and their grades
- Update existing student grades
- Display all student grades

### Key Concepts Used
- **Dictionaries** - For storing key-value pairs
- **if-else statements** - For validation and menu selection
- **Dictionary operations** - Adding, updating, and checking keys
- **File structure** - Function definitions and menu-driven interface

### Core Functions
1. `add_student()` - Add a new student with grade validation
2. `update_student()` - Update existing student's grade
3. `print_all_students()` - Display all stored grades
4. `display_menu()` - Show available options

### Example Execution Steps

**Step 1: Adding Students**
```
Adding Yusuf with grade 82...
Adding Raza with grade 87...
Adding Sayyed with grade 76...
```

**Step 2: Displaying All Grades**
```
STUDENT GRADES LIST
Yusuf: 82
Raza: 87
Sayyed: 76
```

**Step 3: Updating a Grade**
```
Yusuf's current grade: 82
Yusuf's updated grade: 89
```

**Step 4: Final List**
```
FINAL STUDENT GRADES LIST
Yusuf: 89
Raza: 87
Sayyed: 76
Salman: 89
Khan: 33
```

## Program 3: Write to a File

### Description
A program that creates a text file and writes content to it using Python's file handling capabilities.

### Key Concepts Used
- `open()` function with write mode `'w'`
- `file.write()` method to write content
- Context manager `with` statement for automatic file closure
- Error handling with `IOError` and `except` blocks

### File Operations Explained

**Write Mode (`'w'`)**
- Creates a new file or overwrites existing file
- Positions the pointer at the beginning
- Returns a file object

**Using `with` Statement**
- Automatically closes the file after operations
- Ensures proper resource management
- No need to manually call `file.close()`


### Features
- Creates `sample_data.txt` file
- Writes comprehensive content about file operations
- Displays success message
- Shows the written content
- Includes error handling for IOError

### Example Output
```
Success! Content written to 'sample_data.txt'
File location: sample_data.txt

Content written:
--------------------------------------------------
Don't forget that gifts often come with costs that go beyond their purchase price. When you purchase a child the latest smartphone, you're also committing to a monthly phone bill. When you purchase the latest gaming system, 
[Content continues...]
--------------------------------------------------
```

---

## Program 4: Read from a File

### Description
A program that reads and displays content from an existing text file using Python's file reading capabilities.

### Key Concepts Used
- `open()` function with read mode `'r'`
- `file.read()` method to read entire file content
- Context manager `with` statement
- Error handling for `FileNotFoundError`

### File Operations Explained

**Read Mode (`'r'`)**
- Opens file for reading only
- File must exist, otherwise raises `FileNotFoundError`
- Positions pointer at the beginning
- Cannot modify file content

**Reading Methods**
- `file.read()` - Reads entire file as one string
- `file.readline()` - Reads one line at a time
- `file.readlines()` - Reads all lines as a list


### Features
- Reads from `sample_data.txt` (created by Program 3)
- Displays file content
- Handles missing file error gracefully
- Shows helpful message if file doesn't exist

### Example Output
```
Successfully read from 'sample_data.txt'
File location: sample_data.txt

--------------------------------------------------
FILE CONTENT:
--------------------------------------------------
Don't forget that gifts often come with costs that go beyond their purchase price. When you purchase a child the latest smartphone, you're also committing to a monthly phone bill. When you purchase the latest gaming system, 
[Content continues...]
--------------------------------------------------
```
