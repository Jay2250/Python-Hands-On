# Initialize the dictionary to store movie votes
movie_votes = {}


def manage_votes():
    while True:
        print("\n--- Movie Voting System ---")
        print("1. Add a new movie")
        print("2. Vote for a movie")
        print("3. Remove a movie")
        print("4. Display voting results")
        print("5. Find the top movie")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            vote_movie()
        elif choice == '3':
            remove_movie()
        elif choice == '4':
            display_results()
        elif choice == '5':
            find_top_movie()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


def add_movie():
    movie = input("Enter the name of the movie to add: ")
    if movie in movie_votes:
        print(f"'{movie}' already exists in the list.")
    else:
        movie_votes[movie] = 0
        print(f"'{movie}' has been added with 0 initial votes.")


def vote_movie():
    movie = input("Enter the name of the movie to vote for: ")
    if movie in movie_votes:
        movie_votes[movie] += 1
        print(f"Vote added for '{movie}'. Total votes: {movie_votes[movie]}")
    else:
        print(f"'{movie}' is not in the list. Please add it first.")


def remove_movie():
    movie = input("Enter the name of the movie to remove: ")
    if movie in movie_votes:
        del movie_votes[movie]
        print(f"'{movie}' has been removed from the list.")
    else:
        print(f"'{movie}' is not in the list.")


def display_results():
    if movie_votes:
        print("\n--- Current Voting Results ---")
        for movie, votes in movie_votes.items():
            print(f"{movie}: {votes} votes")
    else:
        print("No movies in the list.")


def find_top_movie():
    if movie_votes:
        top_movie = max(movie_votes, key=movie_votes.get)
        print(
            f"The movie with the highest number of votes is '{top_movie}' with {movie_votes[top_movie]} votes.")
    else:
        print("No movies in the list.")


manage_votes()
