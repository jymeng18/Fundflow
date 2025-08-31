from budget import Budget

def main():
    print("Welcome to Fundflow CLI!\n")
    budget = Budget(default_envelopes=["needs", "wants", "savings"])

    while True:
        print("\nOptions:")
        print("1. Add envelope")
        print("2. Deposit money")
        print("3. Spend money")
        print("4. Show balances")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter envelope name: ").strip().lower()
            budget.add_envelope(name)

        elif choice == "2":
            name = input("Which envelope?: ").strip().lower()
            amount = float(input("How much?: "))
            budget.deposit(name, amount)

        elif choice == "3":
            name = input("Which envelope?: ").strip().lower()
            amount = float(input("How much?: "))
            budget.spend(name, amount)

        elif choice == "4":
            budget.print_all_envelopes()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
