from pdfreader import PDFDocument, SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

print(viewer.metadata)

viewer.navigate(59)
viewer.render()
print(viewer.canvas.text_content)
# print(viewer.canvas.strings)

print("===========================================================================")
print("===========================================================================")
print("===========================================================================")

text_content_lines = viewer.canvas.text_content.split('\n')

for i in range(len(text_content_lines)):
    if "TT0" in text_content_lines[i]:
        print("i - 4", text_content_lines[i-4])
        print("i - 3", text_content_lines[i-3])
        print("i - 2", text_content_lines[i-2])
        print("i - 1", text_content_lines[i-1])

# print("".join(viewer.canvas.strings))

print("===========================================================================")
print("===========================================================================")
print("===========================================================================")

for i in range(len(text_content_lines)):
    if "quoad" in text_content_lines[i]:
        print("i - 1", text_content_lines[i - 1])
        print("i - 0", text_content_lines[i])