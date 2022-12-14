for url in urls_lib:
    s_count = 175
    m_count = 175
    l_count = 175

    soup = BeautifulSoup(src, "lxml")
    words_count = 0
    chars_count = 0
    all_chars_count = 0
    article_text = ""
    for tab in soup.select('.article-view > p'):
        article_text += str(tab.text + "\n")
        tab_text = str(tab.text)
        tab_text.replace('-', '')
        words_count += len(re.findall(r'\w+', tab_text))
        all_chars_count += len(tab_text)
        chars_count += len(re.findall(r'\S', tab_text))
    if (words_count > 50) and (words_count < 250):
        if (s_count > 209):
            break
        with open("S/" + str(s_count) + ".txt", "w", encoding="utf-8") as file:
            file.write(f"URL\n07.04.2022\n{words_count}\n{all_chars_count}, {chars_count}\n7\n")
        new_doc = docx.Document()
        new_doc.add_paragraph(article_text)
        new_doc.save("E:/PycharmProjects/S/" + str(s_count) + ".docx")
        s_count += 1
    if (words_count > 251) and (words_count < 900):
        if (m_count > 209):
            break
        with open("M/" + str(s_count) + ".txt", "w", encoding="utf-8") as file:
            file.write(f"URL\n07.04.2022\n{words_count}\n{all_chars_count}, {chars_count}\n7\n")
        new_doc = docx.Document()
        new_doc.add_paragraph(article_text)
        new_doc.save("E:/PycharmProjects/S/" + str(m_count) + ".docx")
        m_count += 1
    if (words_count > 901) and (words_count < 2000):
        if (l_count > 209):
            break
        with open("L/" + str(s_count) + ".txt", "w", encoding="utf-8") as file:
            file.write(f"URL\n07.04.2022\n{words_count}\n{all_chars_count}, {chars_count}\n7\n")
        new_doc = docx.Document()
        new_doc.add_paragraph(article_text)
        new_doc.save("E:/PycharmProjects/S/" + str(l_count) + ".docx")
        l_count += 1


