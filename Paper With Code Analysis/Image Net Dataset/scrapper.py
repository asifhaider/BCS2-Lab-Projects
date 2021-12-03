# test flag
flag = 1
outputs = open('/content/drive/MyDrive/Colab Notebooks/BCS2 Paper With Code/outputs.txt', 'a')

for link in all_links:
    print('====================== Link ' + str(flag) + ' ==========================')
    outputs.write('===================================== Link ' + str(flag) + ' ==================================================' + '\n')
    url = requests.get(link)
    soup = BeautifulSoup(url.content,"html")

    for a in soup.find_all('a', href=True):
        mystr= a['href']
        if(mystr[-4:]=='.pdf'):
            print ("url with pdf final:", a['href'])
            outputs.write("url with pdf final:" + str(a['href']) + '\n')
            urlpdf = a['href']
            response = requests.get(urlpdf)
            with io.BytesIO(response.content) as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()
                txt = f"""
                Author: {information.author}
                Creator: {information.creator}
                Producer: {information.producer}
                Subject: {information.subject}
                Title: {information.title}
                Number of pages: {number_of_pages}
                """
                # Here the metadata of your pdf
                print(txt)
                outputs.write(txt + '\n')
                # numpage for the number page
                numpage=0
                page = pdf.getPage(numpage)
                # data = pdf.getXmpMetadata()
                # data = page.getContents()
                page_content = page.extractText().split('\n')
                for content in page_content:
                  if 'Abstract' in content:
                    break 
                  else:
                    print(content)
                    outputs.write(content + '\n')                    
                # print the content in the page 1           
                # print(page_content)
                # print(data)
    flag = flag + 1
    # if flag>3:
    #   output.close()
    #   break
outputs.close()  