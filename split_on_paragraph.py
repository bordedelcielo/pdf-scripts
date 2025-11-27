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

    text_content_lines = viewer.canvas.text_content.split("/P <<>> BDC")

    paragraph_counter = 1
    for paragraph in text_content_lines:
        print('=====================================')
        print('Paragraph number', paragraph_counter)
        print('\n')
        print(paragraph)
        paragraph_counter += 1