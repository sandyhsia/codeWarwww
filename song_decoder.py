## My
def song_decoder(song):
    list = song.split('WUB')
    new_list = [list[i] for i in range(len(list)) if list[i] != '']
    list = new_list
    result_str = ""
    for i in range(len(list)):
        if i != len(list)-1:
            result_str += list[i]
            result_str += " "
        else:
            result_str += list[i]
    return result_str

## Best
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])