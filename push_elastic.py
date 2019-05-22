from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import csv
from elasticsearch import Elasticsearch
import speech_recognition as sr


def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    filepath.close()
    device.close()
    retstr.close()
    return text


#if __name__ == "__main__":
text = pdf_to_text("File.pdf")
print(text)
f = open('File.txt', 'w')
f.write(text.decode())
f.close()
   
with open('skills.csv', 'r') as f:
    reader = csv.reader(f)
    skills = list(reader)
    
for i in range(len(skills)):
    skills[i] = skills[i][0]

resume_skills = text.decode()

matched_skills = []
for skill in skills:
    if skill.lower() in resume_skills.lower():
        print(skill + ' present')
        matched_skills.append(skill)
        
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es.index(index='resume', doc_type='skills', id=1, body={"skills": matched_skills})

# es.get(index='resume', doc_type='skills', id=1)

recognizer = sr.Recognizer()
audio_file = sr.AudioFile('Recording.wav')
with audio_file as source:
    audio = recognizer.record(source)    
    
recognizer.recognize_google(audio, language='en', show_all=True)
