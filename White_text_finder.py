import pdfplumber

pdf_file = pdfplumber.open('/Users/devmehta/Desktop/dev/Om Prakash Karmacharya1.pdf')
for p, char in zip(pdf_file.pages, pdf_file.chars):
    words = p.extract_words(keep_blank_chars=True)
    texts = p.extract_text()
    print(f"Page Number: {p.page_number}")
    print(f"Font Name: {char['fontname']}")
    print(f"Font Size: {char['size']}")
    print(f"Stroking Color: {char['stroking_color']}")
    print(f"Non_stroking Color: {char['non_stroking_color']}")
    print(texts.strip())
    print('\n')
