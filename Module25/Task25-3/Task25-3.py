class MyDict(dict):

    def get(self, key, default=0):
        return self[key] if key in self else default

d = MyDict()
print(d.get(1))