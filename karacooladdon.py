import requests

SONG_FILE_NAME = ''

def queue_reoder(self):

    index = 0
    reorderArray = []
    counter = {}
    if self.now_playing_user != None:
      counter[self.now_playing_user] = 1

    for item in self.queue:
      if item["user"] in counter:
        counter[item["user"]] += 1
      else:
        counter[item["user"]] = 1
      reorderArray.append([item, counter[item["user"]], index])
      index += 1

    reorderArray.sort(key=lambda x: (x[1], x[2]))

    finalQueue = []
    for reorderLine in reorderArray:
      finalQueue.append(reorderLine[0])

    return finalQueue

def lastfm_data(search_arg):
  
  url = "https://ws.audioscrobbler.com/2.0/?method=track.search&track=" + search_arg + '&api_key=ec023e5f4c7c36e55d3ebd3e933ca8d2&limit=10&format=json'
  try:
    response = requests.get(url)
    data = response.json()  
    tracks = []
    for results in data['results']['trackmatches']['track']:
      title = results['artist'] + ' - ' + results['name']
      tracks.append(title)
  except:
    return None
  
  return tracks