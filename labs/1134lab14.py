from ChainingHashTableMap import *
from DoublyLinkedList import *

def most_frequent(lst):
    hash_map = ChainingHashTableMap()
    for elem in lst:
        if(elem not in hash_map):
            hash_map[elem] = 1
        else:
            hash_map[elem] += 1
    high = -1
    highest = elem
    for key in hash_map:
        if(hash_map[key] > high):
            high = hash_map[key]
            highest = key
    return highest

def first_unique(lst):
    hash_map = ChainingHashTableMap()
    for elem in lst:
        if(elem not in hash_map):
            hash_map[elem] = 1
        else:
            hash_map[elem] += 1
    for key in lst:
        if(hash_map[key] == 1):
            return key
    return None

class PlayList:
    def __init__(self):
        self.data = ChainingHashTableMap()
        self.songs = DoublyLinkedList()
    def add_song(self, new_song_name):
        node = self.songs.add_last(new_song_name)
        self.data[new_song_name] = node
    def add_song_after(self, song_name, new_song_name):
        if(song_name not in self.data):
            raise KeyError()
        node = self.songs.add_after(self.data[song_name], new_song_name)
        self.data[new_song_name] = node
    def play_song(self, song_name):
        if(song_name not in self.data):
            raise KeyError()
        return song_name
    def play_list(self):
        curr = self.songs.header.next
        while(curr is not self.trailer):
            print(curr.data)
            curr = curr.next

def two_sum(lst, target):
    hash_map = ChainingHashTableMap()
    for i, elem in enumerate(lst):
        diff = target - elem
        if(diff in hash_map):
            return (hash_map[diff], i)
        hash_map[elem] = i



    
