import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class BookDisplay:
    def __init__(self, book: Book, display_type: str):
        self.book = book
        self.display_type = display_type

    def display_type_console(self):
        print(self.book.content)

    def display_type_reverse(self):
        print(self.book.content[::-1])

    def display(self) -> None:
        if self.display_type == "console":
            self.display_type_console()
        elif self.display_type == "reverse":
            self.display_type_reverse()
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")


class BookPrint:
    def __init__(self, book: Book, print_type: str):
        self.book = book
        self.print_type = print_type

    def print_type_console(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_type_reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print_book(self) -> None:
        if self.print_type == "console":
            self.print_type_console()
        elif self.print_type == "reverse":
            self.print_type_reverse()
        else:
            raise ValueError(f"Unknown print type: {self.print_type}")


class BookSerializer:
    def __init__(self, book: Book, serialize_type: str):
        self.book = book
        self.serialize_type = serialize_type

    def serializer_type_json(self) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})

    def serializer_type_xml(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self) -> str:
        if self.serialize_type == "json":
            return self.serializer_type_json()
        elif self.serialize_type == "xml":
            return self.serializer_type_xml()
        else:
            raise ValueError(f"Unknown serialize type: {self.serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay(book, method_type)
        elif cmd == "print":
            BookPrint(book, method_type)
        elif cmd == "serialize":
            BookSerializer(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
