# Idea: viewer.canvas.text_content could be split on paragraph. 
# This would make the identification of individual paragraphs much easier.
# From there, paragraphs could be split on '\n', as is currently done for the entire page.

from pdfreader import SimplePDFViewer
from scripts.modules_a import extract_strings

filename = "line_by_line.txt"
with open(filename, 'w') as file:
    file.write("Line by line")

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

ms = ""
segment = ""
for page in range(906, 907):

    viewer.navigate(page)
    viewer.render()

    text_content_lines = viewer.canvas.text_content.split('\n')

    for index, line in enumerate(text_content_lines):
        if index == 400:
            break
        print('\n')
        print("Page:", page, "Index:", index, "Line:\n", line)
        with open(filename, 'a') as file:
            file.write('\n')
            file.write(line)
        strings = extract_strings(line=line, segment=segment)
        if strings != "":
            print(strings)