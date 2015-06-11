from lxml import html
import requests
import json


page = requests.get('http://www.portlandchronicle.com/demolition-permits-issued-may-25-may-31/')
tree = html.fromstring(page.text)


mayTwentyFiveHead = tree.xpath('//*[@id="post-3022"]/div/p[3]/strong/text()')

mayTwentyFiveBlock = tree.xpath('//*[@id="post-3022"]/div/div/p/strong/text()')

mayTwentyFiveFoot = tree.xpath('//*[@id="post-3022"]/div/div/div/p/strong/a/text()')

if u'\xa0' in mayTwentyFiveBlock:
  print "FIX ME"


# print mayTwentyFiveBlock.replace(u'\xa0', "places");

# ["noone" if x==u'\xa0' else x for x in mayTwentyFiveBlock]
# print mayTwentyFiveBlock

# mayTwentyFiveBlock[0] = "boom"



import csv

f = open('zzz.csv', 'w')
writer = csv.writer(f)
writer.writerow([mayTwentyFiveHead[0], "Portland", "OR"])
writer.writerow([mayTwentyFiveFoot[0], "Portland", "OR"])



for i in range(0, len(mayTwentyFiveBlock)):
  if u'\xa0'==mayTwentyFiveBlock[i]:
    mayTwentyFiveBlock[i]="0.0, 0.0"
  writer.writerow([mayTwentyFiveBlock[i], "Portland", "OR"])

f.close()

# str.replace(u'\xa0', ' ').encode('utf-8')

#Include if there are links in address
# may = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p/strong/a/text()')

# mayTwentyFiveBlock.replace(u'\xa0', u' ')
# string.replace('\\xa0', ' ')



print 'May 25 Head: ', mayTwentyFiveHead
# print '     : '
# print len(mayTwentyFiveHead)


# print '     : '

print 'May 25 Block: ', mayTwentyFiveBlock
# print '     : '
# print len(mayTwentyFiveBlock)


# print '     : '

print 'May 25 Foot: ', mayTwentyFiveFoot
# print '     : '
# print len(mayTwentyFiveFoot)


# import csv

# b = open('trying.csv', 'w')
# a = csv.writer(b)

# data = [mayTwentyFiveBlock]

# a.writerows(data)
# b.close()

# f = open('zzz.csv', 'w')
# writer = csv.writer(f)
# writer.writerows([mayTwentyFiveBlock])

# f.close()
