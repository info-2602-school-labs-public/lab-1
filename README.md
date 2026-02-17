# Getting Started

Follow these steps to set up the lab environment and run the development server:

1. **Download the lab files:**  
   - Go to the repository page on GitHub.  
   - Click the **Code** button and select **Download ZIP**.

2. **Extract the zip file** into a folder.

3. **Open the folder in VSCode:**  
   - Make sure the folder you opened is the **parent folder** containing the lab files.

4. **Open the VSCode terminal:**  
   - Menu → Terminal → New Terminal.

5. **For Windows users:**  
   - Ensure the shell is **Command Prompt**, not PowerShell.  
   - If the terminal line starts with `PS`, the shell is incorrect.

6–10. **Run the following commands in order:**

6. **Create a virtual environment**
```bash
python -m venv venv
```
7. **Activate the virtual environment**
# Windows
```venv\Scripts\activate```
# Mac/Linux
```source venv/bin/activate```

8. **Install dependencies**
```pip install -e ".[dev]"```

9. **Start the development server**
```fastapi dev```
# If the default port is in use, run on another port:
```fastapi dev --port 9090```

10. **Open the application in your browser**
# Click the link shown in the terminal; you should see "Hello World"
# If using a custom port:
```http://localhost:9090```

