class Codec:
    
    # User a simple counter 
    def __init__(self):
        self.counter = 0
        self.longToShort = {}
        self.shortToLong = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.longToShort:
            return str(self.longToShort[longUrl])
        else:
            shortUrl = str(self.counter)
            self.longToShort[longUrl] = shortUrl
            self.shortToLong[shortUrl] = longUrl 
            self.counter += 1
            #print("encode:", longUrl, " -> ", shortUrl)
            return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.shortToLong:
            longUrl = self.shortToLong[shortUrl]
            #print("decode:", shortUrl, " -> ", longUrl)
            return longUrl
        else:
            return None
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))