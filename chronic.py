from lxml import html
import requests

page = requests.get('http://www.portlandchronicle.com/demolition-permits-issued-may-25-may-31/')
tree = html.fromstring(page.text)

#This will create a list of buyers:
#address = tree.xpath('//div[@title="buyer-name"]/text()')

# # address = tree.xpath('span[@title="html-tag"]/text()')
# address = tree.xpath('//*[@id="post-3022"]/header/h1/text()')
# title = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[1]/text()')
# name = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[1]/strong/text()')

# # <p data-canvas-width="90.61610071791893">
# name1 = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[2]/text()')

# # <strong>14232 E BURNSIDE ST, 97233</strong>
# name2 = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[2]/strong/text()')


# # <p data-canvas-width="90.61610071791893"> 3810 SE 69th
# name3 = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[4]/text()')


# # <strong>3810 SE 69TH AVE, 97206</strong>
# name4 = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p[4]/strong/text()')

# mayEighteenHead = tree.xpath('//*[@id="post-3022"]/header/h1/text()')
# mayEighteenBlock = tree.xpath('//*[@id="post-3022"]/header/h1/text()')
# mayEighteenFoot = tree.xpath('//*[@id="post-3022"]/header/h1/text()')

mayTwentyFiveHead = tree.xpath('//*[@id="post-3022"]/div/p[3]/strong/text()')

mayTwentyFiveBlock = tree.xpath('//*[@id="post-3022"]/div/div/p/strong/text()')

mayTwentyFiveFoot = tree.xpath('//*[@id="post-3022"]/div/div/div/p/strong/a/text()')



# wrong
# fullList = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/text()')

# name2 = tree.xpath('/text()')

# /html/body/table/tbody/tr[217]/td[2]/span[2]

# print 'Address: ', address
# print 'Title: ', title
# print 'Name: ', name
# print 'Name1: ', name1
# print 'Name2: ', name2
# print 'Name3: ', name3
# print 'Name4: ', name4

# print 'May 18: ', mayEighteen
# print '     : '
# print len(mayEighteen)
# print 'May 25: ', mayTwentyFive


print 'May 25 Head: ', mayTwentyFiveHead
print '     : '
print len(mayTwentyFiveHead)


print '     : '

print 'May 25 Block: ', mayTwentyFiveBlock
print '     : '
print len(mayTwentyFiveBlock)


print '     : '

print 'May 25 Foot: ', mayTwentyFiveFoot
print '     : '
print len(mayTwentyFiveFoot)



# [u' \u2013\xa0Owner: PORTLAND HABILITATION CENTER INC \u2013 Applicant: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013 Contractor: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013 Application received 4/14, permit issued 5/26',
# u' \u2013\xa0Owner: PORTLAND HABILITATION CENTER INC \u2013 Applicant: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013 Contractor: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013 Application received 4/14, permit issued 5/26',
# u' \u2013\xa0Owner: PORTLAND HABILITATION CENTER INC \u2013 Applicant: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013 Contractor: DON SILVEY, SILCO COMMERCIAL CONSTRUCTION INC \u2013\xa0Application received 4/14, permit issued 5/26',
# u' \u2013 Owner: PDX PROPERTY INNOVATIONS LLC and TTM DEVELOPMENT CO \u2013 Applicant: PDX PROPERTY INNOVATIONS LLC \u2013 Contractor: PDX PROPERTY INNOVATIONS LLC \u2013\xa0Application received 4/1, permit issued 5/26',
# u' \u2013 Owner: NT CONSTRUCTION CORP \u2013 Applicant: NT CONSTRUCTION CORP \u2013 Contractor: not listed \u2013 Application received 4/14,\xa0permit issued 5/27', '- Owner: ',
# u'\xa0\u2013 Applicant: ',
# u', FASTER PERMITS \u2013 Contractor: ',
# u'\xa0\u2013 Application received 4/21, permit issued 5/27', u' \u2013 Owner: MARY J WALKER \u2013 Applicant: STEVE EWOLDT, ARTIFEKT ARCHITECTURE + INTERIORS \u2013 Contractor: ',
# u' \u2013 Application\xa0received 3/17, permit issued 5/27',
# u' \u2013 Owner: ',
# u'\xa0\u2013 Applicant: MIKE COYLE, FASTER PERMITS \u2013 Contractor: ',
# u'\xa0\u2013 Application received 4/21,\xa0permit issued 5/27',
# u' \u2013 Owner: ', u'\xa0\u2013 Applicant: ',
# u'\xa0\u2013 Contractor: ',
# u'\xa0\u2013 Application received 4/22, permit issued 5/28']


# Full List:  [
# '14238 E BURNSIDE ST, 97233',
# '14232 E BURNSIDE ST, 97233',
# '25 SE 143RD AVE, 97233',
# '3810 SE 69TH AVE, 97206',
# '10923 NE FREMONT ST, 97220',
# u'\xa0',
# '8249 SE BUSH ST, 97266',
# '820 NE 69TH AVE, 97213',
# '7340 N MACRUM AVE, 97203'
# ]


