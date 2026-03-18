# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 6 - Advanced Music Queue
#
# ~ Created by CMPUT 175 Team ~
# ============================================================

# Install ytmusicapi using pip
from ytmusicapi import YTMusic
from structures import DLinkedListNode, DLinkedList, Song, time_to_seconds
import os

NO_OF_RESULTS = 5

def clear():
    '''
    Clears the screen based on the operating system.
    '''
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def extract_artists(song):
    """
    Input: A dictionary containing song information
    Returns: A string of artist names separated by commas
    Working:
    This function extracts and returns a comma-separated string of artist names from the song dictionary.
    """
    # TODO: Implement this function
    try:
        artists = song['artists']
        artist_names = [artist['name'] for artist in artists]
        return ", ".join(artist_names)
    except:
        return "NA"

def song_search(query):
    """
    Input: Search query
    Returns: Top "NO_OF_RESULTS" i.e. 5 results from the retrieved data
    Working:
    This function invokes the search method on YTMusic object with required arguments
    """
    # TODO: Implement this function
    ytmusic = YTMusic()
    results = ytmusic.search(query, filter="songs")
    return results[:NO_OF_RESULTS]

def filter_info(results):
    """
    Input: Search results in a JSON like format
    Returns: List of Song Objects
    Working:
    This function is supposed to extract the required information from the JSON,
    create Song objects and append them to a list. If an error occurs, raise an
    exception.
    """
    # TODO: Implement this function
    songs = []
    for result in results:
        try:
            name = result['title']
            artist = extract_artists(result)
            duration = time_to_seconds(result['duration'])
            song = Song(name, artist, duration)
            songs.append(song)
            
        except:
            raise Exception("An error occurred while filtering")
    return songs

def print_song_results(results):
    """
    Input: A list of Song objects
    Returns: None
    Working:
    This function prints the list of Song objects in a formatted manner.
    """
    assert type(results[0]) == Song, "The list to be printed doesn't have the items of type 'Song'"

    print("RESULTS:")
    for i in range(len(results)):
        print(f"{i+1}. {results[i]}")

def search():
    """
    Input: None
    Return: A Song object representing the song the user wants to add into the Queue, or None if the user wants to go back
    Working:
    1. This function takes search query from the user
    2. Searches for the song using song_search function
    3. Filters the information using filter_info function
    4. Prints the song results using print_song_results function
    5. Asks for user choice
    6. Returns the chosen song information
    7. If the user wants to go back, it returns None
    """
    # TODO: Implement this function
    song_title = input("Search: ")

    song_results = song_search(song_title)
    filtered_results = filter_info(song_results)
    print_song_results(filtered_results)
    
    choice_str = """Choose one of the following options:
                \tEnter a number (1-5) to add a song to playlist
                \tEnter '0' to search again
                \tEnter 'q' to go back
            """
    print(choice_str)
    selected_song = False
    i = 0
    while not selected_song:
        if i > 0:
            print('Invalid Input.')
        choice = input(f">> ")
        if choice in ['0', 'q'] or (choice.isdigit() and 1 <= int(choice) <= len(filtered_results)):
            selected_song = True
        i = 1

    if choice.lower() == 'q':
        return None
    elif choice == '0':
        return search()
    else:
        return filtered_results[int(choice) - 1]

def main():
    """
    Initializes the music queue and provides an interactive menu to manage songs.
    Users can add songs, navigate to next or previous songs, remove the current song,
    display or clear the queue, and quit the program.

    NOTE: You need to modify the main function to use the DLinkedList class to manage the music queue. 
          Add the new features that are needed for this Lab assignment as per the description.

          ** MAKE SURE YOU READ THE DESCRIPTION CAREFULLY AND UNDERSTAND THE REQUIREMENTS. **
    """
    queue = DLinkedList()
    clear()
    print("WELCOME")
    choice_str = """Choose one of the following options:
                \t1. Add Song
                \t2. Next Song
                \t3. Previous Song
                \t4. Remove Current Song
                \t5. Show Queue
                \t6. Clear Queue
                \t7. Quit
                Enter the choice (eg: 2)
                """
    contBuild = True
    try:
        while contBuild:

            print('Currently playing:')
            if queue.is_empty() == False: 
                print('  ',queue.get_current(),'\n')
            else: 
                print('  ',"None",'\n')

            print(choice_str)
            choice = input('>> ')
            while choice not in ['1','2','3','4','5','6','7']:
                print('Invalid Input.')
                choice = input('>> ')
            
            if choice == '1':
                clear()
                song = search()
                if song != None:
                    if queue.is_empty():
                        queue.add_last(song)
                    else:
                        place = input("Where would you like to add the song:\n\t1. Add Next\n\t2. Add to the End\n>> ")
                        while place not in ['1','2']:
                            print('Invalid Input.')
                            place = input('>> ')
                        
                        if place == '1':
                            queue.add_next(song)
                        elif place == '2':
                            queue.add_last(song)
                    print("Song added successfully!")
                    input("\nPress enter key to continue...")

            elif choice == '2':
                clear()
                if queue.is_empty():
                    print("Queue is empty.")
                else:
                    current_before = queue.get_current()
                    queue.play_next()
                    current_after = queue.get_current()

                    if current_before == current_after:
                        print("No next song in the queue.")
                    else:
                        print('Now playing:')
                        print("  ",queue.get_current())

                input("\nPress enter key to continue...")

            elif choice == '3':
                clear()
                if queue.is_empty():
                    print('Queue is empty.')
                else:
                    current_before = queue.get_current()
                    queue.play_previous()
                    current_after = queue.get_current()

                    if current_before == current_after:
                        print('No previous song in the queue.')
                    else:
                        print('Now playing:')
                        print("  ",queue.get_current())

                input("\nPress enter key to continue...")

            elif choice == '4':
                clear()
                if queue.is_empty():
                    print('Queue is empty.')
                else:
                    removed_song = queue.remove_current()
                    print("Removed song:")
                    print("  ",removed_song)
                    if queue.is_empty():
                        print('The queue is now empty.')
                    else:
                        print('Now playing:')
                        print("  ",queue.get_current())
                
                input("\nPress enter key to continue...")

            elif choice == '5':
                clear()
                try:
                    print(queue)
                    input("\nPress enter key to continue...")
                except Exception as e:
                    print(e)
            
            elif choice == '6':
                clear()
                queue.clear()
                print('The queue has been cleared!')
                input("\nPress enter key to continue...")

            elif choice == '7':
                contBuild = False
            
            clear()

    except Exception as e:
        print(e)

    print("Thanks for listening!")

if __name__ == "__main__":
    main()