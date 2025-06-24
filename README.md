# Auto-Resume-Generator
A resume generator which transforms your raw text into a downloadable resume 

---

##  Features
- **Images are attached at the bottom**
- Paste raw text into the box
- Extracts Name, Email, Skills, Experience, Education using basic NLP (which is natural language processing)
- Choose between Modern, Classic, and Minimal resume designs
- Downloads a clean resume (pdf form)

---

##  Tech Stack

| Tool         | Purpose                         |
|--------------|---------------------------------|
| Python       |  backend logic              |
| spaCy        | NLP & named entity extraction   |
| Streamlit    | Frontend UI                     |
| Jinja2       | Resume HTML templating          |
| pdfkit       | HTML to PDF conversion          |
| wkhtmltopdf  | PDF rendering engine            |
| HTML/CSS     | Resume styling templates        |

**spacy pretrained model** : 'en_core_web_sm' is a pretrained small english NLP model that includes NER (named entity recognition), we use it to identify person, org, email, etc


---

## How it works

1. You first input your details into the box in a simple and clean format
2. The app basically reads and understands the text
3. We use a language tool called spacy to extract details from the box
4. We put all the extracted data into a dictionary, so the app knows what's a skill,experience,name,etc
5. The user picks a resume style
6. The app takes those details and fills them in the template they chose (those were readymade templates, had to keep it simple)
7. We use a tool called wkhtmltopdf (i will provide the steps to download it below, and then it converts the html resume to a downloadable pdf

---

# Modern Template : 
![](relative/path/to/image.png)
![](relative/path/to/image.png)


# Classic Template :
![](relative/path/to/image.png)
![](relative/path/to/image.png)


# Minimal Template : 
![](relative/path/to/image.png)
![](relative/path/to/image.png)










---

## Installations
run these in your vs code terminal
- pip install streamlit
- pip install spacy
- pip install pdfkit
- pip install jinja2
- python -m spacy download en_core_web_sm

Download wkhtmltopdf (https://wkhtmltopdf.org/downloads.html), just download the installer, start the download, open your file folder, search for bin, copy the path of it, go to 'edit environment variables', select path, click new, paste the path in this, click ok on all windows

Open command prompt : paste this [wkhtmltopdf --version]
it should be there


AUTHOR : PARAM VARSHA (24/06/2025)





