"""
Zadanie 1
"""

class Document:
    def __init__(self):
        self.lista = []

    def add_element(self, klasa):
        self.lista.append(klasa)
        pass

    def render(self):
        plik = ""
        with open("text.md", "wt") as fd:
            for element in self.lista:
                plik += element.render() + "\n"
                fd.writelines(element.render() + "\n")

        return print(plik)

class Element:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class HeaderElement:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"{self.text}\n{'=' * len(self.text)}"

class LinkElement:
    def __init__(self, nazwa, link):
        self.nazwa = nazwa
        self.link = link

    def render(self):
        return f"({self.nazwa})[http://{self.link}]"


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()
