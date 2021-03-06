# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
from janome.dic import UserDictionary
from sysdic import SYS_DIC

print('Compile user dictionary (MeCab IPADIC format)')
user_dict = UserDictionary("user_ipadic.csv", "utf8", "ipadic", SYS_DIC.connections)
user_dict.save("/tmp/userdic")

t = Tokenizer("/tmp/userdic")
for token in t.tokenize(u'東京スカイツリーへのお越しは、東武スカイツリーライン「とうきょうスカイツリー駅」が便 利です。'):
  print(token)


print('')
print('Compile user dictionary (simplified format)')
user_dict = UserDictionary("user_simpledic.csv", "utf8", "simpledic", SYS_DIC.connections)
user_dict.save("/tmp/userdic_simple")

t = Tokenizer("/tmp/userdic_simple")
for token in t.tokenize(u'東京スカイツリーへのお越しは、東武スカイツリーライン「とうきょうスカイツリー駅」が便 利です。'):
  print(token)
