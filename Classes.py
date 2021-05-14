


class Employee:
    def __init__(self,eid,enm,esal,eag,erole,eadr):
        self.empId=int(eid)
        self.empName=enm
        self.empAge=int(eag)
        self.empSalary=float(esal)
        self.emoRole=erole
        self.empAddress=eadr

    def __str__(self):
        return f'''\n\n {self.__dict__}'''

    def __repr__(self):
        return str(self)

class Role:
    def __init__(self,rid,rcode,rname):
        self.roleId = rid
        self.roleCode = rcode
        self.roleName = rname

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


class Address:
    def __init__(self,city,state,pincode):
        self.city=city
        self.state=state
        self.pincode=pincode

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str (self)

import random

ROLELIST=['SSE','SE','MANAGER','CEO','STAFF','HOUSEKEEPING','LEAD']

role_count=0
def get_dummy_role():
    global role_count
    role_count=role_count + 1
    ROLE = ROLELIST[random.randint(0,len(ROLELIST)-1)]
    return Role(rid=role_count,rcode=ROLE+str(role_count),rname=ROLE)


adr_count=1000
ADDRESSLIST=['PUNR','MUMBAI','SATARA','SANGALI','YAVATMAL','PUSAD']
def get_dummy_address():
    global adr_count
    adr_count=adr_count+1
    city=ADDRESSLIST([random.randint(0,len(ADDRESSLIST)-1)])
    return Address (city,state='MH',pincode=random.raindint(111111,9999999))


emp_count=777
def get_dummy_employee(n):
    global emp_count
    emp_count= emp_count+1
    emplist=[]
    for item in range(n):
        name=f'{chr(random.randint(65,90))}AAAA'
        age=random.randint(22,60)
        salary =round(random.randint(30000,8000)/3,2)
        adr_list=[]
        for adr in range(random.randint(1,5)):
            adr_list.append=(get_dummy_address())

        roles =[]
        for adr in range(random.randint(1,3)):
            roles.append(get_dummy_employee())

        emplist.append(Employee(eid=emp_count,enm=name,age=age,
                                esal=salary,erole=roles,eadr=adr_list))
    return emplist
epmlist=get_dummy_employee(10)
























