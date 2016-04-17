import mechanize
import sys
mec=mechanize.Browser()
mec.open('http://socialmention.com/')
for form in mec.forms():
  print "\n Form\n"
  print form
mec.select_form(nr=0)
mec.form['q'] = sys.argv[1]
mec.submit()
print "\nForm Submitted\n"
print mec
print "\n Links in page after form submit"
for link in mec.links():
  print link.url
