### **Function: `findLine`**

This function is designed to locate specific lines in a configuration file based on a header name and/or a starting string. It reads the configuration file and outputs details about the location of the requested line or header.

---

### **Parameters**
1. **`config`**:
   - The file path to the configuration file.
   - Defaults to `.pyscripts` if no file is specified (handled externally).

2. **`line`**:
   - A string that specifies the start of the line to search for.

3. **`head`**:
   - The header name to search for in the configuration file.

---

### **Workflow**

#### **1. File Handling**
- Opens the provided configuration file in read mode.
- If the file is not found, calls the `FileNotFound()` function.

---

#### **2. Line-by-Line Processing**
- Iterates through the lines of the configuration file:
  - **Header Identification**:
    - If a line starts with `[py.` and matches the provided `head`, the header is identified, and its line number is printed.
    - Tracks whether a header has been found using `headerFound`.
  - **Line Search**:
    - Checks if the line starts with the given `line` string.
    - If found, prints its line number and associates it with the most recently identified header.
  - Updates `header` to store the current header name.

---

#### **3. Output Messages**
- **Success**:
  - Displays the line and header details if the specified line and/or header is found.
- **Errors**:
  - Reports if:
    - The line is not found.
    - The header is not found.
    - Both the line and the header are missing.

---

### **Key Features**
1. **Header Context**:
   - Associates the found line with its enclosing header.
   - Indicates which header the line belongs to.
2. **Dynamic Defaults**:
   - Uses `.pyscripts` as the default configuration file (handled by external logic if `config` is missing).
3. **Error Handling**:
   - Identifies missing headers, lines, or both.
   - Calls `FileNotFound()` for missing configuration files.

---

### **Example Workflow**

#### **Input Configuration File (`.pyscripts`)**
```
# Line Of Configuration (LOC) file = .pyscripts
[py.test]
build=python setup.py build
install=python setup.py install
[py.deploy]
start=python main.py
```

#### **Function Call**
```python
findLine(".pyscripts", "install", "test")
```

#### **Output**
```
Found 'test' @ line 2
Found 'install=python setup.py install' @ line 3 in test
```

#### **Another Call**
```python
findLine(".pyscripts", "start", "deploy")
```

#### **Output**
```
Found 'deploy' @ line 5
Found 'start=python main.py' @ line 6 in deploy
```

---

### **Error Scenarios**
1. **Line Not Found**
   ```python
   findLine(".pyscripts", "update", "deploy")
   ```
   **Output**:
   ```
   Found 'deploy' @ line 5
   Line not found @ .pyscripts
   ```

2. **Header Not Found**
   ```python
   findLine(".pyscripts", "build", "config")
   ```
   **Output**:
   ```
   Header not found @ .pyscripts
   ```

3. **Both Line and Header Missing**
   ```python
   findLine(".pyscripts", "update", "config")
   ```
   **Output**:
   ```
   Line and header not found @ .pyscripts
   ```
