import json, random, string, uuid, locale, datetime, re
from uuid import UUID


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)

customers={}

i=1

while (i<1001):

    def getRandomString(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return(result_str)

    def phoneNo():
        d1=random.choice([2,9])
        min = pow(10, 6 - 1)
        max = pow(10, 6) - 1
        z=random.randint(min, max)
        if d1==2:
            d2=random.choice([2,3,4,5,6])
            no=str(d1)+str(d2)+str(z)
            return(no)

        elif d1==9:
            d2=random.choice([9,5,6,7])
            no=str(d1)+str(d2)+str(z)
            return(no)

    def postal():
        filePo='/home/mike/Desktop/supermarket/postal-codes.csv'
        f= open(filePo, 'r')
        a=[]
        a=f.readlines()
        i=0
        while i<1000:
            s = random.choice(a)
            regex=re.compile(r'[\n\t]')
            n=regex.sub(" ",s)
            l=[*range(1,70,1)]
            a=n+"Number "+str(random.choice(l))
            return (a)
        i+=1


    def locales():
        v=locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return(v)

    def dateCreated():
        today=datetime.datetime.now()
        return(str(today))

    def email():
        letters = string.ascii_lowercase
        l=[]
        g=random.choice([5,6,7,8,9,10,11,12,13])
        result_str = ''.join(random.choice(letters) for i in range(g))
        e = ["@gmail.com", "@yahoo.com","@icloud.com","@outlook.com","@hotmail.com","@hotmail.net","@cytanet.com.cy","@cablenet.com.cy","@primetel.com.cy","@aol.com","@aol.net","@yandex.net"]
        e1=random.choice(e)
        e2=str(result_str)
        e3=str(e1)
        return(e2 + e3)

    def salesOrders():
        x=1-2

    customers[i]={
    'customerid': uuid.uuid4(),
    'name': getRandomString(random.randint(10,20)),
    'phone': phoneNo(),
    'adress': postal(),
    'locale': locales(),
    'date&timeCreated': dateCreated(),
    'emailAdress':  email(),
    'salesOrders': salesOrders()
    }

    i+=1
s=json.dumps(customers,indent=3, separators=(',', ': '), cls=UUIDEncoder)

with open ("/home/mike/Desktop/supermarket/customers.json", 'w') as f:
    f.write(s)

