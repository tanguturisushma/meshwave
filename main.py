from cpu_ram import get_resource_usage, display_resource_usage


def main():
    print("\n===== MESHWAVE PROJECT =====")
    print("1. Check CPU and RAM usage")
    print("2. Exit")
    print("Please select an option from the menu.")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        resources = get_resource_usage()
        display_resource_usage(resources)

    elif choice == "2":
        print("Thank you for using Meshwave!")

    else:
        print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()