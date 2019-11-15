from pprint import pprint as pp

d = {'two':[1,2,3,{'inner':"is here!", 'one more':[1,2,3]},7,8,9,'string is here!',(1,)],'one':'just string'}
pp(d, depth=1)
