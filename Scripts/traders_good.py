from dir import *
import random
f = open('TraderGoods.ini', 'w', encoding='utf-8-sig')
tr1 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr2 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr3 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr4 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr5 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr6 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr7 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr8 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr9 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr10 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr11 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr12 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr13 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr14 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]
tr15 =[random.choice(goods_novice), random.choice(goods_skilled), random.choice(goods_veteran), random.choice(goods_master)]

f.write("""
[Medic]
Trader1=True
Trader2=True
Trader3=True
Trader4=True
Trader5=True
Trader6=True
Trader7=True
Trader8=True
Trader9=True
Trader10=True
Trader11=True
Trader12=True
Trader13=True
Trader14=True
Trader15=True

""")
for i in goods:
    f.write(f"""[{i}]
Trader1={''.join([str(True) if i in tr1 else str(False)])}
Trader2={''.join([str(True) if i in tr2 else str(False)])}
Trader3={''.join([str(True) if i in tr3 else str(False)])}
Trader4={''.join([str(True) if i in tr4 else str(False)])}
Trader5={''.join([str(True) if i in tr5 else str(False)])}
Trader6={''.join([str(True) if i in tr6 else str(False)])}
Trader7={''.join([str(True) if i in tr7 else str(False)])}
Trader8={''.join([str(True) if i in tr8 else str(False)])}
Trader9={''.join([str(True) if i in tr9 else str(False)])}
Trader10={''.join([str(True) if i in tr10 else str(False)])}
Trader11={''.join([str(True) if i in tr11 else str(False)])}
Trader12={''.join([str(True) if i in tr12 else str(False)])}
Trader13={''.join([str(True) if i in tr12 else str(False)])}
Trader14={''.join([str(True) if i in tr12 else str(False)])}
Trader15={''.join([str(True) if i in tr12 else str(False)])}

""")
f.close()