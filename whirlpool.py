%%time
%%memit

import whirlpool
print('----------- Whirlpool Implementation---------------')
text = input('Enter the data: ')
print("Original data: " + text)
hashObject = whirlpool.new(text.encode('utf-8'))
digest = hashObject.hexdigest()
print("After applying Whirlpool Hash Function:")
print(digest)