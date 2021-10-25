def songs_time_sum(number):
    print('Название', number + 1, '-й песни: ', end= ' ')
    song_name = input()
    for song in violator_songs:
        if song_name == song[0]:
            return song[1]
def start():
    songs_amount = int(input('Сколько песен выбрать? '))
    songs_time = 0
    for number in range(songs_amount):
        songs_time += songs_time_sum(number)
    return songs_time


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_time = start()       
            
print('Общее время звучания песен: ', round(songs_time, 2), 'минут')
