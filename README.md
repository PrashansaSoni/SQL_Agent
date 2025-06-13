#  SQL Agent

This project enables users to query a MySQL database using **plain English questions**. It leverages the **Groq LLM** with **LangChain** to translate natural language into SQL queries and fetch real-time results.

---

## 🚀 Features

- Ask database questions in English (e.g., "What is the total quantity of apples sold in April?")
- Translates English into SQL queries using Groq LLM
- Executes SQL on a MySQL database
- Clean, terminal-friendly results
- Simple CLI interface

---

## 🗂 Project Structure

├── run.py              
├── sql_agent.py          
├── .env                  
├── requirements.txt     
└── README.md             

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PrashansaSoni/SQL_Agent.git
cd SQL_Agent
```
### 2. Create virtual enviroment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. create .env file
```bash
GROQ_API_KEY=your_groq_api_key
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=mydb
```
### 4. Run
```bash
python run.py
```

### Example
```sql
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100),
    quantity INT,
    sale_date DATE
);

INSERT INTO sales (product, quantity, sale_date) VALUES
('Apples', 50, '2024-04-10'),
('Oranges', 20, '2024-04-12'),
('Apples', 30, '2024-04-20');

```
