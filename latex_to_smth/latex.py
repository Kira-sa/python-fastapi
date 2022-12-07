from pylatex import Document, Eqref


def make_document():
    doc = Document('basic')
    add_function(doc)

    doc.generate_tex()
    doc.generate_pdf()


def add_function(doc, income="y=a/b"):
    with make_document(Eqref()) as eq:
        eq.add_item("y = a + b")
    doc.append(f"${income}$")
    doc.append(f"\({income}\)")
    doc.append(f"\[{income}\]")



if __name__ == '__main__':
    make_document()
