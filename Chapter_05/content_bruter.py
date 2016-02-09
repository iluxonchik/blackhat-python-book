import threading
import urllib
import urllib

threads = 50
target_url = "http://testphp.vulnweb.com"
wordlist_file = "all.txt" # from SVNDigger
resume = None # used in case of network connectivity failures
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"

def build_wordlist(wordlist_file):
    # read in the wordlist
    fd = open(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()
    
    found_resume = False
    words = Queue.Queue()
    
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist from: {0}".format(resume))
        else:
            words.put(word)
    return words