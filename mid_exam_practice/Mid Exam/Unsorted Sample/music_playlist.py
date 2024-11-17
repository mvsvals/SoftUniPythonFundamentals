
input_songs = input().split()
total_commands = int(input())

for command in range(total_commands):
    input_command = input().split(' * ')
    if input_command[0] == 'Add Song':
        song = input_command[1]
        if song not in input_songs:
            input_songs.append(song)
            print(f"{song} successfully added")
    elif input_command[0] == 'Delete Song':
        number_of_songs = int(input_command[1])
        if len(input_songs) > number_of_songs:
            print(', '.join(input_songs[:number_of_songs]) + ' deleted')
            input_songs[:number_of_songs] = []
    elif input_command[0] == 'Shuffle Songs':
        song_index_one = int(input_command[1])
        song_index_two = int(input_command[2])
        if 0 <= song_index_one <= len(input_songs) - 1 and 0 <= song_index_two <= len(input_songs) - 1:
            input_songs[song_index_one], input_songs[song_index_two] = input_songs[song_index_two], input_songs[song_index_one]
            print(f"{input_songs[song_index_one]} is swapped with {input_songs[song_index_two]}")
    elif input_command[0] == 'Insert':
        song = input_command[1]
        index = int(input_command[2])
        if 0 <= index <= len(input_songs) - 1:
            if song in input_songs:
                print("Song is already in the playlist")
            else:
                input_songs.insert(index, song)
                print(f"{song} successfully inserted")
        else:
            print("Index out of range")
    elif input_command[0] == 'Sort':
        input_songs.sort(reverse=True)
    elif input_command[0] == 'Play':
        print("Songs to play:")
        print(*input_songs, sep='\n')
