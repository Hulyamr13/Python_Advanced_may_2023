class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls((photos_count + 3) // 4)

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"

        return "No more free slots"

    def display(self):
        photos = ["-" * 11]

        for row in self.photos:
            photos.append(("[] " * len(row)).rstrip())
            photos.append("-" * 11)

        return '\n'.join(photos)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
