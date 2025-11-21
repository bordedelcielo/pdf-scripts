from pdfreader import SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

file_name = "debug_italics.txt"
with open(file_name, 'w') as file_object:
    file_object.write("Debug Italics Logs")

for page in range(905, 920):

    viewer.navigate(page)
    viewer.render()

    text_content_lines = viewer.canvas.text_content.split('\n')

    # print("Page Number", page)
    for index, line in enumerate(text_content_lines):
        with open(file_name, 'a') as file_object:
            file_object.write('\n')
            file_object.write("Page = " + str(page) + " " + "Index = " + str(index) + " " + "|" + " " + line)