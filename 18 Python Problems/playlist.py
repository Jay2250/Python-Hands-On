playlist = []


def add_songs():
    try:
        songs = input("Enter song titles (comma-separated): ").split(',')
        # here strip removes extra spaces from the single string
        songs = [song.strip() for song in songs]
        playlist.extend(songs)
        print(f"Songs added to the playlist: {songs}")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_song():
    try:
        song = input("Enter the song title to remove: ").strip()
        if song in playlist:
            playlist.remove(song)
            print(f"'{song}' has been removed from the playlist.")
        else:
            print(f"'{song}' is not in the playlist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_songs():
    if playlist:
        print("Playlist:", ", ".join(playlist))
    else:
        print("The playlist is empty.")


def slice_playlist():
    try:
        start = int(input("Enter the start index: "))
        end = int(input("Enter the end index: "))
        if start < 0 or end > len(playlist):
            print("Indices out of range.")
        else:
            print(f"Sliced playlist: {playlist[start:end]}")
    except ValueError:
        print("Invalid input. Please enter integers for the indices.")
    except Exception as e:
        print(f"An error occurred: {e}")


def playlist_manager():
    while True:
        print("\n--- Music Playlist Manager ---")
        print("1. Add songs")
        print("2. Remove song")
        print("3. View all songs")
        print("4. Slice playlist")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_songs()
        elif choice == '2':
            remove_song()
        elif choice == '3':
            view_songs()
        elif choice == '4':
            slice_playlist()
        elif choice == '5':
            print("Exiting the playlist manager.")
            break
        else:
            print("Invalid choice. Please try again.")


playlist_manager()
