# -*- coding: utf-8 -*-


import idcard_recognize;


s=1
d=30
#rand=[]
#rand1=[]
#for s in [1,2,3]:
#    for d in [21,22,23,24,25,26,27,28,29]:
'''
sum=[]
result=idcard_recognize.process('testimages/test.jpg',s,d)
if result['address']!='山西省翼城县八一南路唐兴小区二巷6号':sum.append('test')

result=idcard_recognize.process('testimages/1.jpg',s,d)
if result['address']!='哈尔滨市南岗区人和街75号5单元601户':sum.append('1')

result=idcard_recognize.process('testimages/2.jpg',s,d)
if result['address']!='湖南省邵阳县五峰铺镇白田村下尤铺组17号':sum.append('2')

result=idcard_recognize.process('testimages/3.jpg',s,d)#name对，address错，名丢了
if result['address']!='福建省南平市延平区黄墩排垅巷21幢2室':sum.append('3')

result=idcard_recognize.process('testimages/4.jpg',s,d)
if result['address']!='河南省信阳市平桥区五里镇凤台村143号':sum.append('4')

result=idcard_recognize.process('testimages/5.jpg',s,d)
if result['address']!='四川省新津县花源镇官林村5组':sum.append('5')

result=idcard_recognize.process('testimages/6.jpg',s,d)
if result['address']!='河北省唐山市玉田县鸦鸿桥镇邢庄村宏亮街9号':sum.append('6')

result=idcard_recognize.process('testimages/7.jpg',s,d)
if result['address']!='成都市成华区圣灯乡崔家店村2组2栋4单元1号':sum.append('7')

result=idcard_recognize.process('testimages/8.jpg',s,d)
if result['address']!='重庆市丰都县名山镇白沙沱村3组':sum.append('8')

result=idcard_recognize.process('testimages/9.jpg',s,d)
if result['address']!='广州市越秀区东风西路195号':sum.append('9')

result=idcard_recognize.process('testimages/10.jpg',s,d)
if result['address']!='甘肃省兰州市城关区东岗东路1989号802':sum.append('10')

result=idcard_recognize.process('testimages/11.jpg',s,d)
if result['address']!='长春市南关区卫星路11号':sum.append('11')

result=idcard_recognize.process('testimages/13.jpg',s,d)
if result['address']!='安徽省宿州市埇桥区曹村镇梅庄村三组343号':sum.append('13')

result=idcard_recognize.process('testimages/14.jpg',s,d)
if result['address']!='天津市红桥区郭辛庄新建里11号':sum.append('14')

result=idcard_recognize.process('testimages/15.jpg',s,d)
if result['address']!='辽宁省大连市甘井子区海茂路807号144':sum.append('15')

result=idcard_recognize.process('testimages/jsy.jpg',s,d)
if result['address']!='山西省翼城县八一南路唐兴小区二巷6号':sum.append('jsy')
        #rand.append(len(sum))
        #rand1.append((s,d))
print(sum)
#print(rand)
#print(rand1)
'''

#print(idcard_recognize.process('testimages/cqr.jpg'));#实验民族为非1个字的
print(idcard_recognize.process('testimages/cqjsy.jpg'));#实验民族为非1个字的
#print(idcard_recognize.process('testimages/test.jpg'));
#print(idcard_recognize.process('testimages/1.jpg'));
#print(idcard_recognize.process('testimages/2.jpg'));
#print(idcard_recognize.process('testimages/3.jpg'));
print(idcard_recognize.process('testimages/4.jpg'));
print(idcard_recognize.process('testimages/5.jpg'));
#print(idcard_recognize.process('testimages/6.jpg'));
#print(idcard_recognize.process('testimages/7.jpg'));
#print(idcard_recognize.process('testimages/8.jpg'));
#print(idcard_recognize.process('testimages/9.jpg'));
#print(idcard_recognize.process('testimages/10.jpg'));
#print(idcard_recognize.process('testimages/11.jpg')); 
#print(idcard_recognize.process('testimages/13.jpg'));
#print(idcard_recognize.process('testimages/14.jpg'));
#print(idcard_recognize.process('testimages/15.jpg'));
#print(idcard_recognize.process('testimages/jsy.jpg'));
