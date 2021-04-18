# html_to_pdf
html to pdf converter using python
Steps to use tha converter

**Installation:**

Install pisa using "pip install xhtml2pdf" command

**How to use the function**

#context passed must **dictionary** as shown below for the sample file

context = {'{Heading}':'HTML TO PDF CONVERTER','{first_name}':'Tushar', '{last_name}':'Nachan' }

from utils import convert_html_to_pdf

path = '/sample.html' #path of html file
#calling the function

convert_html_to_pdf(path, 'output.pdf', context=context)
