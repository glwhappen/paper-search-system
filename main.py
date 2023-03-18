import os

from file import get_files, calculate_file_md5
import pdf


def get_pdf():
    """
    获取pdf文件内容
    :return:
    """
    files = get_files("pdf")
    pdfs = []
    for file in files:
        pdfs.append({
            'file': file,
            'content_list': pdf.read(file),
            'md5': calculate_file_md5(file),
        })
    return pdfs


def search(content):
    """
    在文章中搜索单词
    :param content:
    :return:
    """
    pass
    pdfs = get_pdf()
    result = {}
    for pdf in pdfs:
        # print(pdf['file'], pdf['md5'])
        file_md5 = pdf['md5']
        for clist in pdf['content_list']:
            # print(clist['page_num'])
            # print(clist)
            for text in clist['text_list']:
                sentense = text.split('<EOL>')
                for s in sentense:
                    if s.find(content) != -1:
                        # print(s)
                        if file_md5 not in result:
                            result[file_md5] = {
                                'file': pdf['file'],
                                'search': [
                                    {
                                        'page_num': clist['page_num'] + 1,
                                        'sentense': s
                                    }
                                ]
                            }
                        else:
                            result[file_md5]['search'].append({
                                'page_num': clist['page_num'] + 1,
                                'sentense': s
                            })
    return result


if __name__ == '__main__':
    # print(get_pdf())
    # print(search('cognitive'))

    search_data = search('cognitive')
    for file_md5 in search_data:
        print("所在位置", search_data[file_md5]['file'])
        search_list = search_data[file_md5]['search']
        for search_content in search_list:
            print(search_content['sentense'], f"第{search_content['page_num']}页")

    # python找出一个单词在文章中的位置，并输出所在句子
    # 1. 找出单词在文章中的位置
