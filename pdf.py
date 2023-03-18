import re

import PyPDF2

def read(file):
    # 打开 PDF 文件
    pdf_file = open(file, 'rb')

    # 创建一个 PDF 阅读器对象
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # 获取 PDF 文件的页数
    num_pages = pdf_reader.getNumPages()
    result = []
    # 遍历每一页并读取内容
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        # print(text)
        result.append({
            'page_num': page_num,
            'text_list': deal_text(text)
        })

    # 关闭 PDF 文件
    pdf_file.close()
    return result

def reg_sentense(matched):
    # print(f"match[{matched.group()}]")
    return matched.group().replace(' ', '<EOL>')

def deal_text(text):
    """
    对pdf进行处理
    将断掉的换行进行拼接
    :return:
    """
    pass

    text = text.replace('-\n', '')
    # text = text.replace('\S\n\S', ' ')
    text = re.sub('[a-z,]\n[a-z]', ' ', text)
    text = re.sub('e.g.\n[a-z]', ' ', text)
    text = re.sub('\)\n[a-z]', ' ', text)
    text = re.sub(';\n[a-z]', ' ', text)

    text = re.sub('[a-zA-Z]\.(?P<space>[ ])[A-Z]', reg_sentense, text)

    return text.split('\n')


if __name__ == '__main__':
    pass
    print(read('./pdf/Wu 等 - Cognitive Modelling for Predicting Examinee Perfor.pdf')[0]['text'])
