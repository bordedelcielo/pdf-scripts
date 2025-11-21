from pdfreader import PDFDocument, SimplePDFViewer
from itertools import islice

# italics = page_59.Resources.Font["TT0"]

# print("====================================================")
# print("====================================================")
# print("====================================================")

# print(italics.items())

fd = open("my_ebook/one_of_my_ebooks.pdf", "rb")
viewer = SimplePDFViewer(fd)

# print(viewer.metadata)

viewer.navigate(915)
viewer.render()
# print(viewer.canvas.text_content)
# print(viewer.canvas.strings)

# print("===========================================================================")
# print("===========================================================================")
# print("===========================================================================")

text_content_lines = viewer.canvas.text_content.split('\n')

def print_lines():
    for index, line in enumerate(text_content_lines):
        if "  " in line:
            break
        print('\n')
        print(index, line)

# print_lines()

# for i in range(len(text_content_lines)):
#     if "TT0" in text_content_lines[i] and "nos" in text_content_lines[i - 1]:
#         print("===========================================================================")
#         print("i - 9", text_content_lines[i-9])
#         print("i - 8", text_content_lines[i-8])
#         print("i - 7", text_content_lines[i-7])
#         print("i - 6", text_content_lines[i-6])
#         print("i - 5", text_content_lines[i-5])
#         print("i - 4", text_content_lines[i-4])
#         print("i - 3", text_content_lines[i-3])
#         print("i - 2", text_content_lines[i-2])
#         print("i - 1", text_content_lines[i-1])
#         print("i - 0", text_content_lines[i])

# print("".join(viewer.canvas.strings))

def find_bdc():
    for index, line in enumerate(text_content_lines):
        # print('\n')
        # print("index:", index)
        # print("line:", line)
        if "  " in line:
            break
        elif "/P <<>> BDC" in line:
            print('\n')
            print("index + 0", text_content_lines[index + 0])
            print("index + 1", text_content_lines[index + 1])
            print("index + 2", text_content_lines[index + 2])
            print("index + 3", text_content_lines[index + 3])
            print("index + 4", text_content_lines[index + 4])
            print("index + 5", text_content_lines[index + 5])
            print("index + 6", text_content_lines[index + 6])
            print("index + 7", text_content_lines[index + 7])
            print("index + 8", text_content_lines[index + 8])
            print("index + 9", text_content_lines[index + 9])
            print("index + 10", text_content_lines[index + 10])
        if " tj" in line.lower() and "8" in line:
            print('\n')
            print("index + 0", text_content_lines[index + 0])
            print("index + 1", text_content_lines[index + 1])
            print("index + 2", text_content_lines[index + 2])
            print("index + 3", text_content_lines[index + 3])
            print("index + 4", text_content_lines[index + 4])
            print("index + 5", text_content_lines[index + 5])
            print("index + 6", text_content_lines[index + 6])
            print("index + 7", text_content_lines[index + 7])
            print("index + 8", text_content_lines[index + 8])
            print("index + 9", text_content_lines[index + 9])
            print("index + 10", text_content_lines[index + 10])

# find_bdc()

def print_new_paragraph():
    for index, line in enumerate(text_content_lines):
        if "  " in line:
            break
        elif "BDC" in line and "Td" in text_content_lines[index + 2] + text_content_lines[index + 3]: # This appears to be capable of catching new paragraphs.
            print('\n')
            print(text_content_lines[index + 3] + text_content_lines[index + 4])

# print_new_paragraph()



def run_page():
    page_text = ""
    segment = ""
    for idx, i in enumerate(text_content_lines):
        # print(i)
        # if "0.895 -1.15 Td" in i or "-15.82 -1.15 Td" in i:
        if "-1.15 Td" in i:
            print('\n')
            # print(i)
            try:
                print("idx - 2", text_content_lines[idx - 2])
                print("idx - 1", text_content_lines[idx - 1])
                print("idx + 0", text_content_lines[idx])
                print("idx + 1", text_content_lines[idx + 1])
            except:
                print("Can't print i[idx + 1]")
        if "TT0" in i or "T1_0" in i or "TT1" in i or "  " in i:
            # print(i)
            # print(segment)
            page_text += segment
            segment = ""
            if "  " in i:
                # print("\nEnding\n")
                break
        if "tj" in i[-2:].lower():
            if i[0] == "(":
                # print('\n')
                # print(i)

                for index in range(1, len(i) - 4):
                    if i[index] == "\\":
                        pass
                    else:
                        segment += i[index]

            elif i[0] == "[":
                queue = []
                # print('\n')
                # print(i)

                for index in range(1, len(i) - 4):
                    if i[index] == "(" and i[index - 1] != "\\":
                        queue.append("(")
                    elif i[index] == ")" and i[index - 1] != "\\":
                        queue.pop()
                    elif i[index] == "\\":
                        pass
                    elif queue == ["("]:
                        segment += i[index]
    return page_text

# print(run_page())

# doc = PDFDocument(fd)

# page_59 = next(islice(doc.pages(), 58, 59))

# print(page_59)

# print("====================================================")
# print("====================================================")
# print("====================================================")

# print(sorted(page_59.Resources.Font.keys()))

footnote = False

for index, line in enumerate(text_content_lines):
    if footnote == True:
        print(index, line)
    # if footnote == True and line == "/Span <<>> BDC":
    #     print('\n')
    #     print(index + 0, text_content_lines[index + 0])
    #     print(index + 1, text_content_lines[index + 1])
    #     print(index + 2, text_content_lines[index + 2])
    #     print(index + 3, text_content_lines[index + 3])
    #     print(index + 4, text_content_lines[index + 4])
    #     print(index + 5, text_content_lines[index + 5])
    #     print(index + 6, text_content_lines[index + 6])
    #     print(index + 7, text_content_lines[index + 7])
    #     print(index + 8, text_content_lines[index + 8])
    #     print(index + 9, text_content_lines[index + 9])
    #     print(index + 10, text_content_lines[index + 10])
    else:
        if "  " in line:
            print('\n')
            print(line)
            print(sorted(list(set(list(line)))))
            if sorted(list(set(list(line)))) == [' ', '(', ')', 'T', 'j']:
                footnote = True