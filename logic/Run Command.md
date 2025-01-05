### **Logic of the Function `runScript`**

The `runScript` function is designed to execute a script or set of commands from a configuration file based on a specified header and (optionally) a command token. It processes the configuration file line-by-line and executes the relevant commands.

---

### **Parameters**
1. **`run_cmd`**:
   - A string containing the header name (e.g., `header`) or header and token (e.g., `header.command_token`).
   - If omitted, the user is prompted to input the header name.

2. **`config_file`**:
   - Path to the configuration file.
   - Defaults to `.pyscripts` if not provided.

3. **`pipe`**:
   - Boolean flag indicating whether to execute commands using `subprocess` with a pipe for input/output.

---

### **Steps**

#### **1. Default Configuration File**
- If no `config_file` is provided, `.pyscripts` is used.
- The function attempts to read the file:
  - If the file is missing, the `FileNotFound()` function is called.
  - If the file exists but is not a valid LOC (Line Of Configuration) file, it writes a header indicating the LOC format.

---

#### **2. Parse the `run_cmd`**
- **Header & Token Extraction**:
  - If `run_cmd` contains a period (`.`), it splits the string:
    - **Header**: The part before the `.`.
    - **Token**: The part after the `.`.

- **Header Display**:
  - Prints the header and token information.

---

#### **3. Line-by-Line Processing**
- Loops through each line in the configuration file:
  - **Header Validation**:
    - Checks if the line starts with `[py.` and matches the specified header.
    - Ensures unexpected headers are flagged as errors.
  - **Command Line Parsing**:
    - If the line contains `=` and matches the token (if provided), the corresponding command is added to the `cmd` list.
  - **Comment Lines**:
    - Lines starting with `#` are ignored.

---

#### **4. Error Handling**
- Handles scenarios where:
  - Header is not found.
  - Command token does not match.
  - Syntax errors in the configuration file.

---

#### **5. Execute Commands**
- Extracts commands from the `cmd` list.
- **Command Execution**:
  - Displays the commands to be executed.
  - If `pipe` is `True`, uses `subprocess.run` for command execution and captures output.
  - Otherwise, uses `os.system` for direct execution.

---

### **Output Messages**
- **Header/Command Information**:
  - Displays header and token details.
  - Reports missing headers or commands.
- **Execution Details**:
  - Number of commands to execute.
  - Executes each command, showing success or error status.

---

### **Key Features**
- **Default Behavior**:
  - Uses `.pyscripts` if no config file is specified.
- **Flexibility**:
  - Supports headers with or without tokens.
- **Error Handling**:
  - Identifies missing headers, commands, and syntax issues.
- **Command Execution**:
  - Offers `subprocess.run` or `os.system` for flexibility in execution.

---

### **Example Usage**
#### **Input:**
- Config file `.pyscripts`:
  ```
  # Line Of Configuration (LOC) file = .pyscripts
  [py.test]
  build=python setup.py build
  install=python setup.py install
  ```
- Command: `runScript("test.install", ".pyscripts", True)`

#### **Output:**
```
Config file: .pyscripts
Header: [py.test]
Command token: install

Header found @ line 2: [py.test]
Token value: python setup.py install

Number of commands executing: 1

Commands:
python setup.py install

Executing Commands...

Executing: python setup.py install
All Commands Executed
```