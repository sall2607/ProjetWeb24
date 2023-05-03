
def base_donnee_trigramme(files):
    #Import library
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import CountVectorizer
    import re 
    """
    # summarize & generating output"""
    # Remove stop words and white spaces
    stop = stopwords.words('english')
    stop1= stopwords.words('french')
    c=stop+stop1
    files['nom Maladie'] =  files['nom Maladie'].apply(lambda x: " ".join(x for x in x.split() if x not in c))
    files['nom Maladie']  =files['nom Maladie'] .apply(lambda x: re.sub(' [\s]', ' ', x))
    files['nom Maladie']  =files['nom Maladie'] .apply(lambda x: re.sub(' [\n]', ' ', x))
    files['nom Maladie']  =files['nom Maladie'] .apply(lambda x: re.sub(' [^\w]', ' ', x))
    files['nom Maladie'] = files['nom Maladie'] .apply(lambda x: re.sub('[{!@#$:).;?}&]', '', x.lower()))
    files['nom Maladie']  =files['nom Maladie'] .apply(lambda x: re.sub(' ', ' ', x))

    #mettre les données en trigrammme
    nomMaladie =list( files['nom Maladie'])
    vectorizer1 = CountVectorizer(ngram_range=(3,3))
    # tokenizing
    vectorizer1.fit(nomMaladie)
    # encode document
    vector = vectorizer1.transform(nomMaladie)
    l1= vectorizer1.vocabulary_.keys()
    return l1 



def papier_trigramme(test):
    import re 
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd

    stop = stopwords.words('english')
    stop1= stopwords.words('french')
    c=stop+stop1
    
    #nettoyage
    df = pd.DataFrame({'donnees':test})
    df['donnees'] =  df['donnees'].apply(lambda x: b" ".join(x for x in x.split() if x not in c))
    df['donnees']  =df['donnees'] .apply(lambda x: re.sub(' [^\w]', ' ', str(x)))
    df['donnees']  =df['donnees'] .apply(lambda x: re.sub(' [\s]', ' ',  str(x)))
    df['donnees']  =df['donnees'] .apply(lambda x: re.sub('[\n] ', ' ', str(x)))
    df['donnees']= df['donnees'].apply(lambda x: re.sub('[{!@#$:.;?}&]', '', str(x.lower())))
    df['donnees']  =df['donnees'] .apply(lambda x: re.sub(' ', ' ', str(x)))
    #mettre les données en trigrammme
    nomMaladie1 =list( df['donnees'] )
    vectorizer = CountVectorizer(ngram_range=(3,3))
    # tokenizing
    vectorizer.fit(nomMaladie1)
    # encode document
    vector = vectorizer.transform(nomMaladie1)
    l = vectorizer.vocabulary_.keys()
    return l 


def papier_trigrammes(test):
    
    import re 
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd

    stop = stopwords.words('english')
    stop1= stopwords.words('french')
    c=stop+stop1
    #nettoyage
    d1="".join(x for x in test.split() if x not in c)
    d2=re.sub(' [^\w]', ' ', d1)
    d3=re.sub(' [\s]', ' ',  d2)
    d4=re.sub('[\n] ', ' ', d3)
    d5=re.sub('[{!@#$:.;?}&]', '', d4.lower())
    d6=re.sub(' ', ' ', d5)
    #mettre les données en trigrammme
    nomMaladie1 =list( d6 )
    vectorizer = CountVectorizer(ngram_range=(3,3))
    # tokenizing
    vectorizer.fit(d6)
    # encode document
    vector = vectorizer.transform(nomMaladie1)
    l = vectorizer.vocabulary_.keys()
    return l 


def ConversionToText(fichier):
    import os 
    root,extension= os.path.splitext(fichier)
    if extension=='.pdf' :
        import PyPDF2
        from PyPDF2 import PdfFileReader
        #Creating a pdf file object
        pdf = open(fichier,"rb")
        #creating pdf reader object
        pdf_reader = PyPDF2.PdfReader(pdf)
        #checking number of pages in a pdf file
        num= len(pdf_reader.pages)
        #print(pdf_reader.numPages)
        print(num)
        #creating a page object
        page = pdf_reader.pages[num-1]
        #finally extracting text from the page
        res=page.extract_text()
        print(res)

        newfile = open(r"pdftotext.txt", "w")
        newfile.writelines( res)

        #closing the pdf file
        pdf.close()
        return str(res)
    elif extension == '.docx':
        from docx import Document
        #Creating a word file object
        doc = open("file.docx","rb")
        #creating word reader object
        document = Document(doc)
        docu=""
        for para in document.paragraphs:
            docu += para.text
        newfile = open(r"pdftotext.txt", "w")
        newfile.writelines(docu)
        return docu
    elif extension == '.txt':
        newfile = open(r"pdftotext.txt", "r")
        l=newfile.readlines()
        return "".join(l)
    else:
        print("Error:type de fichier non reconnu")
        
 



import pandas as pd
fichier= pd.read_csv(r'C:\Users\diamo\Downloads\mesDonnees (1).csv')
l1=base_donnee_trigramme(fichier)
print(l1)


test=[]
with open(r"C:\Bureau\GLSI3\PFE\Maladies\pdftotext.txt","rb") as f:
    for i in f :
        test.append(i)
l=papier_trigramme(test)
print(l)


fichier=r"C:\Bureau\GLSI3\PFE\Maladies\pdftotext.txt"
re=ConversionToText(fichier)

test=[]
with open(r"C:\Bureau\GLSI3\PFE\Maladies\pdftotext.txt","rb") as f:
    for i in f :
        test.append(i)

l=papier_trigramme(test)
