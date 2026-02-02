# cli.py
from agent import get_answer

def main():
    while True:
        print("\n\n-----------------------------------")
        question = input("Ask your question (q to quit): ").strip()
        print("\n\n-----------------------------------")
        if question.lower() == "q":
            break
        print(get_answer(question))

if __name__ == "__main__":
    main()
