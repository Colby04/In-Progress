# My Professional Webpage

Hey there! Welcome to my first independent HTML + CSS project— a simple and professional webpage I designed to introduce myself and showcase some of what I’ve learned so far.

---

## About This Project

This webpage serves as my personal online portfolio. I built it from scratch using only HTML and CSS to demonstrate my understanding of structure, styling, and responsive design fundamentals.

The goal was to create something minimal yet professional — a space that reflects both my technical progress and who I am as a person.

---

## Features

- Clean and semantic HTML structure  
- Custom CSS styling  
- Responsive layout for mobile and desktop  
- Links to my **GitHub** and **LinkedIn** profiles  
- Contact information for professional networking  

---

## About Me

My name is **Colby Rhodes**, and I currently work as a **Quality Assurance Analyst at Shipt**, where I’ve been part of the team for over four years.  
I began my coding journey in the summer of 2024 through an edX bootcamp with **Michigan State University**, completing it in **January 2025**.  

Technology and software engineering have always fascinated me — I love exploring how things work behind the scenes and continuously improving my skills.

When I’m not coding, you’ll probably find me:
- Watching documentaries 
- Researching topics that catch my curiosity 
- Spending time with my family and two cats 
- Or traveling (in 2023, I even took a solo trip to Melbourne, Australia)

---

## Professional Links and Contact

- [GitHub Repository](https://github.com/Colby04)  
- [LinkedIn Profile](https://www.linkedin.com/in/colby-rhodes2025)  
- Email: [cjcodes2024@gmail.com](mailto:cjcodes2024@gmail.com)

---

## How to View this Webpage

You can view the webpage by opening the `index.html` file in your browser or by hosting it using GitHub Pages:

1. Clone the repository:  
   ```bash
   git clone https://github.com/Colby04/My-Professional-Webpage.git
    ```

---

## Python demos (folder: `python.demo`)

My project includes a small Python isolated environment in `python.demo` with:
- `demo.api.py` — a tiny Flask API with an HTML homepage and JSON endpoints.
- `expense_tracker.py` — a simple JSON-backed expense tracker.
- `shipment_tool.py` — a small utility demonstrating classes and time math.
- `requirements.txt` — pinned dependencies (Flask).
- `.gitignore` — ignores `.venv` and Python caches for a clean repo.

### Quick start

From the repo root:

```zsh
cd "python.demo"
python3 -m venv .venv
".venv/bin/python" -m pip install --upgrade pip
".venv/bin/pip" install -r requirements.txt
```

Notes
- The virtual environment lives in `python.demo` and is ignored by git.
- You can safely delete and recreate it any time using the commands above.

### Run the Flask demo API (`demo.api.py`)

Start the server:

```zsh
cd "python.demo"
".venv/bin/python" demo.api.py
```

Open in your browser:
- HTML homepage (lists items): http://127.0.0.1:5000/
- All items (JSON): http://127.0.0.1:5000/items
- Single item (JSON): http://127.0.0.1:5000/items/1

Add an item (POST JSON):

```zsh
curl -X POST http://127.0.0.1:5000/items \
   -H "Content-Type: application/json" \
   -d '{"name":"Bananas","price":1.25}'
```

Optional: run via Flask’s CLI (with auto-reload):

```zsh
".venv/bin/python" -m flask --app demo.api run --debug
```

Troubleshooting
- Port already in use: stop the previous server (Ctrl+C) or run on a different port:
   ```zsh
   ".venv/bin/python" -m flask --app demo.api run --debug --port 5050
   ```
- Exit code 137: the process was killed (often due to a port conflict or manual kill). Free the port and re-run.

### Run the Expense Tracker (`expense_tracker.py`)

This script appends expenses to a JSON file `expense_tracker.json` and prints a summary.

```zsh
cd "python.demo"
".venv/bin/python" expense_tracker.py
```

What happens
- Creates or updates `expense_tracker.json` with demo entries.
- Prints a total and per-category breakdown to the terminal.

### Run the Shipment Tool (`shipment_tool.py`)

```zsh
cd "python.demo"
".venv/bin/python" shipment_tool.py
```

Expected output
- Calculates and prints the average delivery time based on sample shipments.

