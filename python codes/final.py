import urllib2
import re
import time
import os

###The input is got as 'user_inp' and checking the input

user_inp = raw_input("Enter the url :")
try:
	website = urllib2.urlopen(user_inp)
	html = website.read()
except NameError as e:
	print ('Not a valid URL!')
	exit()
except urllib2.URLError as e:
	print ('Not a valid URL!')
	exit()
except ValueError as e:
	print ('Not a valid URL!')
	exit()

###Finding the links for the First time

links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
links = '\n'.join(links)
print (links)
f = open('links.txt','w')
f.writelines("%s" %links)

###Checking the Internal Links and storing

u = user_inp.split('.')
f= open('links.txt', 'r')
f2 = open('internal_links.txt', 'w')
for line in f.readlines():
    if re.search(u[1], line):
        print line
        f2.write(line)
f.close
f2.close


###Check The duplicate list

f1 = open('internal_links.txt', 'r')
f2 = open('duplicate_remove.txt', 'w')

lines_seen = set() # holds lines already seen

for line in f1:
    if line not in lines_seen: # not a duplicate
        f2.write(line)
        lines_seen.add(line)

f1.close()
f2.close()


### Checking the Directory & slicing the links 

f1 = open('duplicate_remove.txt','r')
f2 = open('response.txt', 'w')
def everything_between(text,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()

for url in f1.readlines():
	try:
		b = url.replace("'><","")
		b = url.replace(";","")
		b = url.replace("</script>","")
           	b=urllib2.urlopen(b)
		content=b.read()
		title=everything_between(content,'<title>','</title>')
        	if(b.getcode()==200 and title.find('Index') == 0 ):
                	f2.write(url)
			f2.write("\n")
			print url
		sp = url.rsplit('/',1)
   		#print(sp[0])
		b=urllib2.urlopen(sp[0])
		content=b.read()
		title=everything_between(content,'<title>','</title>')
        	while(b.getcode()==200 and title.find('Index') == 0 ):
                	f2.write(sp[0])
			f2.write("\n")
			print(sp[0])			
			sp = sp[0].rsplit('/',1)
   			#print(sp[0])
			b=urllib2.urlopen(sp[0])
			content=b.read()
			title=everything_between(content,'<title>','</title>')          		
	except urllib2.HTTPError as e:
		print e 
	except IndexError as e:
		print e
	except ValueError as e:
		print e
	except urllib2.URLError as e:
		print e
f1.close
f2.close


### Duplication Removal need to be done 

f1 = open('response.txt', 'r')
f2 = open('final.txt', 'w')

lines_seen = set() # holds lines already seen

for line in f1:
    if line not in lines_seen: # not a duplicate
        f2.write(line)
        lines_seen.add(line)

f1.close()
f2.close()



### Downloads the directory

f = open('final.txt','r')
for url in f.readlines():
	cmd = "wget --read-timeout=10 --reject='index.html*' -r --no-parent "
        cmd = cmd + url
	os.system(cmd)  
	print cmd
f.close()
