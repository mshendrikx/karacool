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
