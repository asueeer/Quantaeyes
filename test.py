import re

brief_detail = '<a href="//www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>', re.S)
dd = dr.sub('', brief_detail)
print(dd)
