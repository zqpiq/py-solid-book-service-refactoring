from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, object]]) -> None | str:
    result = None
    for cmd, strategy in commands:
        if cmd == "display":
            strategy.display(book)
        elif cmd == "print":
            strategy.print(book)
        elif cmd == "serialize":
            result = strategy.serialize(book)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", ReverseDisplay()),
                ("serialize", XmlSerializer())
            ]
        )
    )
