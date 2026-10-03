def greet(name: str = "World") -> None:
    print(f"Hello, {name}!")


if __name__ == "__main__":
    user_name = input("Enter your name: ") or "World"
    greet(user_name)
