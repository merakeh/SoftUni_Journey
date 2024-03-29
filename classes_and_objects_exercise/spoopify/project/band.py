from classes_and_objects_exercise.spoopify.project.album import Album
from classes_and_objects_exercise.spoopify.project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for current_album in self.albums:
            if current_album.published:
                return "Album has been published. It cannot be removed."
            if current_album.name == album_name:
                self.albums.remove(current_album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for al in self.albums:
            result.append(al.details())
        return '\n'.join(result)



