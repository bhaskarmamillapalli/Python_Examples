#.format(): used to format the output that is being printed.
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')

print("insert another string with curly brackets :{}".format('the inserted string'))
print("this is a format string {p}".format(p='Example'))
print("one {p},two {p},three {p}".format(p='Day'))
print("a={p},b={q},c={r}".format(p=1,q=3.2,r="hi"))
print('FirstName:{}''MiddleName:{}''LastName:{}'.format('Guido','Van','Rossum'))
print('firstname:{} middlename:{} lastname:{}'.format('Guido','Van','Rossum'))
print('firstname:{1} Middlename:{0} lastname:{2}'.format('Van','Guido','Rossum'))
