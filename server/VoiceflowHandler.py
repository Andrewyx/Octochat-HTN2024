import pickle

debug = {"ids":["123901", "fehwio", "new stuff as well"]}

def storeData(ids: dict) -> None:    
    # Its important to use binary mode
    dbfile = open('cachedIDs.txt', 'wb+')
    # source, destination
    pickle.dump(ids, dbfile)                    
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('cachedIDs.txt', 'rb')    
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

# Debug Storage file
if __name__ == '__main__':
    storeData(debug)
    loadData()


def delete_cache() -> None:
    # Clears the local and remote files
    clear_voiceflow()
    clear_local_files()

def clear_voiceflow() -> None:
    # TODO: For ZACH
    pass

def clear_local_files() -> None:
    # TODO: Clear files then ids
    pass