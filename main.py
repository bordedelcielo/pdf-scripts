from pdfreader import SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

page_html = ""
footer_html = ""
segment = ""
paragraph_queue = []

for page in range(905, 920):

    viewer.navigate(page)
    viewer.render()

    text_content_lines = viewer.canvas.text_content.split('\n')

    for index, line in enumerate(text_content_lines):
        if "  " in line:
            if sorted(list(set(list(line)))) == [' ', '(', ')', 'T', 'j']:
                break

        if "/P <<>> BDC" == line:
            paragraph_queue.append(0)
        elif " td" in line.lower() and paragraph_queue != []:
            segment += "</p><p>"
            paragraph_queue.pop()

        elif "TT0" in line or "T1_0" in line or "TT1" in line or "  " in line:
            if "TT0" in line and segment != "":
                print('\n')
                print("segment:\n", segment)
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

    page_html += segment
    segment = ""

# Open the file in 'write' mode ('w'). If the file exists, its content will be overwritten.
# If the file does not exist, a new one will be created.
with open("my_file.html", "w") as file:
    file.write(page_html + '\n' + footer_html)

print("Content written to my_file.txt (overwriting if it existed).")