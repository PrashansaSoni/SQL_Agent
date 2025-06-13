
from sql_agent import ask_sql_agent

if __name__ == "__main__":
    print("Ask your database in English")
    while True:
        user_input = input(">>> ")
        if user_input.lower() in ("exit", "quit"):
            break
        try:
            response = ask_sql_agent(user_input)
            print(f"\n{response}\n")
        except Exception as e:
            print(f" Error: {e}")
