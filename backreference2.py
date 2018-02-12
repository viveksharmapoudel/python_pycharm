import  re

randstr="https://www.youtube.com http://www.google.com"

#<a href ='https://www.youtube.com'>www.youtube.com</a>
#<a href ='https://www.google.com'> www.google.com</a>

regex= re.compile(r"(https?://([\w.]+))")

randstr=re.sub(regex,r"<a href='\1'>\2</a>\n",randstr)
print(randstr)
