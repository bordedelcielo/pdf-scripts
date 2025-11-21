from pdfreader import SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

viewer.navigate(917)
viewer.render()

text_content_lines = viewer.canvas.text_content.split('\n')

page_html = ""
segment = ""
segment_queue = []
paragraph_queue = []
for index, line in enumerate(text_content_lines):
    if "  " in line:
        print('\n')
        print(line)
        print(sorted(list(set(list(line)))))
        if sorted(list(set(list(line)))) == [' ', '(', ')', 'T', 'j']:
            break
    if "/P <<>> BDC" == line:
        paragraph_queue.append(0)
    elif " td" in line.lower() and paragraph_queue != []:
        segment += "</p><p>"
        paragraph_queue.pop()

    elif "TT0" in line or "T1_0" in line or "TT1" in line or "  " in line:
        if "TT0" in line and segment != "":
            segment = "<i>" + segment + "</i>"
        else:
            pass
        page_html += segment
        segment = ""

    elif " tj" == line.lower()[-3:]:
        if paragraph_queue != []:
            paragraph_queue.pop()
        print("\n")
        print(line)
        # if segment_queue == []:
        #     segment_queue.append(0)
        # else:
        #     page_html += segment
        #     segment = ""
        #     segment_queue.pop()
        if line[0] == "(":

            for index in range(1, len(line) - 4):
                if line[index] == "\\":
                    pass
                else:
                    segment += line[index]

        elif line[0] == "[":
            queue = []
            # print('\n')
            # print(i)

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

print("===================================")
print("\n")
print(page_html)

# Open the file in 'write' mode ('w'). If the file exists, its content will be overwritten.
# If the file does not exist, a new one will be created.
with open("my_file.html", "w") as file:
    file.write(page_html)

print("Content written to my_file.txt (overwriting if it existed).")