from pdfreader import SimplePDFViewer

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

file_name = "debug_superscript.txt"
with open(file_name, 'w') as file_object:
    file_object.write("Debug Superscript Logs")

span_queue = []
superscripts = {}

for page in range(905, 920):

    viewer.navigate(page)
    viewer.render()

    text_content_lines = viewer.canvas.text_content.split('\n')

    # print("Page Number", page)
    for index, line in enumerate(text_content_lines):

        if line == "/Span <<>> BDC":
            span_queue.append(0)
        elif line[-3:].lower() == " tj":
            if span_queue != []:
                num = line[1:-4]
                stripped_num = num.strip()
                # print("page number: ", page, "line:", stripped_num)
                if page not in superscripts:
                    superscripts[page] = []
                superscripts[page].append(stripped_num)
                span_queue.pop()
                with open(file_name, 'a') as file_object:
                    file_object.write('\n')
                    file_object.write("Page = " + str(page) + " " + "Index = " + str(index) + " " + "|" + " " + stripped_num + '-')

for key, value in superscripts.items():
    print("key:", key, "|", "value:", value)