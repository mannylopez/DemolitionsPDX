from lxml import html
import requests

page = requests.get('http://www.portlandchronicle.com/demolition-permits-issued-may-18-may-24/')
tree = html.fromstring(page.text)


mayEighteenHead = tree.xpath('//*[@id="post-2931"]/div/p[3]/strong/text()')

mayEighteenBlock = tree.xpath('//*[@id="post-2931"]/div/div[2]/p/strong/text()')

mayEighteenFoot = tree.xpath('//*[@id="post-2931"]/div/div[2]/p/strong/text()')


# mayTwentyFiveHead = tree.xpath('//*[@id="post-3022"]/div[1]/p[3]/strong/text()')

# mayTwentyFiveBlock = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/p/strong/text()')

# mayTwentyFiveFoot = tree.xpath('//*[@id="post-3022"]/div[1]/div[2]/div/p/strong/a/text()')


# print 'May 25 Head: ', mayTwentyFiveHead
# print '     : '
# print len(mayTwentyFiveHead)


# print '     : '

# print 'May 25 Block: ', mayTwentyFiveBlock
# print '     : '
# print len(mayTwentyFiveBlock)


# print '     : '

# print 'May 25 Foot: ', mayTwentyFiveFoot
# print '     : '
# print len(mayTwentyFiveFoot)

print 'May 18 Head: ', mayEighteenHead
print '     : '
print len(mayEighteenHead)


print '     : '

print 'May 18 Block: ', mayEighteenBlock
print '     : '
print len(mayEighteenBlock)


print '     : '

print 'May 18 Foot: ', mayEighteenFoot
print '     : '
print len(mayEighteenFoot)

