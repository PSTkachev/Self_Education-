def field(record, label):
    for (fname, fvalue) in record:
        if fname==label:
            return fvalue 
bob = [['name','bob smith'],['age',42],['pay',10000]]
print(field(bob,'age'))
#поехавшая функция, работает как словарь
