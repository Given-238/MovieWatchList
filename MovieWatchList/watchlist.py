# Movie Watchlist Manager

movies = []  # Empty list to store movies


def load_movies():
    try:
        with open("movies.txt", "r") as file:
            for line in file:
                movies.append(line.strip())
        print("Movies loaded successfully!\n")
    except FileNotFoundError:
        print("No saved watchlist found. Starting fresh.\n")


def save_movies():
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")
    print("Watchlist saved!\n")


def add_movie():
    movie = input("Enter movie name: ")
    movies.append(movie)
    print(f"'{movie}' added!\n")


def remove_movie():
    movie = input("Enter movie name to remove: ")
    if movie in movies:
        movies.remove(movie)
        print(f"'{movie}' removed!\n")
    else:
        print("Movie not found.\n")


def view_movies():
    if not movies:
        print("Your watchlist is empty.\n")
    else:
        print("\n--- YOUR MOVIE WATCHLIST ---")
        for m in movies:
            print("• " + m)
        print()


def menu():
    load_movies()
    
    while True:
        print("MOVIE WATCHLIST MANAGER")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. View Watchlist")
        print("4. Save Watchlist")
        print("5. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            remove_movie()
        elif choice == "3":
            view_movies()
        elif choice == "4":
            save_movies()
        elif choice == "5":
            save_movies()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()