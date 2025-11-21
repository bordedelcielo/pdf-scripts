from pdfreader import SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

filename = "footnotes.txt"

with open(filename, 'w') as file_object:
    file_object.write("Footnotes")

page_html = ""
footer_html = ""
segment = ""
paragraph_queue = []

for page in range(905, 920):
    is_footnote = False

    viewer.navigate(page)
    viewer.render()

    text_content_lines = viewer.canvas.text_content.split('\n')

    for index, line in enumerate(text_content_lines):
        if "  " in line:
            if sorted(list(set(list(line)))) == [' ', '(', ')', 'T', 'j']:
                is_footnote = True

        if is_footnote == True:
            with open(filename, 'a') as file_object:
                file_object.write('\n')
                file_object.write("Page = " + str(page) + " " + "Index = " + str(index))
                file_object.write('\n')
                file_object.write(line)
            
            if "6.48 0 0 6.48 72 " in line:
                page_html += segment
                segment = ""
                page_html += "</p><p>"

            elif "TT0" in line or "T1_0" in line or "TT1" in line or "  " in line:
                if "TT0" in line and segment != "":
                    segment = "<i>" + segment + "</i>"
                else:
                    pass
                page_html += segment
                segment = ""

            elif " tj" == line.lower()[-3:]:
                if line in ["(CD compiled by the Centre for Culture, Technology and Values, Mary Immaculate College, Limerick, Ireland) Tj", "(Distributed by THE WAY, Campion Hall, Oxford, OX1 1QS. the.way@campion.ox.ac.uk) Tj"]:
                    pass
                else:
                    if paragraph_queue != []:
                        paragraph_queue.pop()
                    if line[0] == "(":
                        for index in range(1, len(line) - 4):
                            if line[index] == "\\":
                                pass
                            else:
                                segment += line[index]
                    elif line[0] == "[":
                        queue = []
                        for index in range(1, len(line) - 4):
                            if line[index] == "(" and line[index - 1] != "\\":
                                queue.append("(")
                            elif line[index] == ")" and line[index - 1] != "\\":
                                queue.pop()
                            elif line[index] == "\\":
                                pass
                            elif queue == ["("]:
                                segment += line[index]

with open("footnotes.html", "w") as file:
    file.write(page_html)