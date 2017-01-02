import MySQLdb

db = MySQLdb.connect(host = "127.0.0.1",
                     user = "root" ,
                     passwd = "110707",
                     db = "db1")
cur = db.cursor()
db.begin()
ch = input("enter 1 to access provider details and enter 2 to access subscriber details")
if(ch==1):
    ch2=input("enter 1 tp insert,2 to delete,3 to view")
    if(ch2==1):
        n = input("enter the number of providers u want to enter :")
        i = 0
        while (i<n):
            
            service = input("enter service")
            name = input("enter name")
            age =input("enter age ")
            i = i+1
            cur.execute("INSERT INTO PROVIDERS VALUES ('%s' ,'%s ','%s') "% (service,name,age))
        cur.execute("SELECT * FROM PROVIDERS")
        for row in cur.fetchall():
            print row
    elif(ch2==2):
        n = input("enter the number of providers u want to delete :")
        i = 0
        while (i<n):
            dname = input("enter name of the provider to delete")
            cur.execute("DELETE FROM PROVIDERS WHERE name = '%s' "% (dname))
            i = i+1;
        cur.execute("SELECT * FROM PROVIDERS")
        for row in cur.fetchall():
            print row
    elif(ch2==3):
        cur.execute("SELECT * FROM PROVIDERS")
        for row in cur.fetchall():
            print row
    else:
        print ("invalid choice")
elif(ch==2):
    ch2=input("enter 1 tp insert,2 to delete,3 to view")
    if(ch2==1):
        n = input("enter the number of subscribers u want to enter :")
        i = 0
        while (i<n):
            
            id1 = input("enter id")
            name = input("enter name")
            age =input("enter age ")
            i = i+1
            cur.execute("INSERT INTO SUBSCRIBERS VALUES ('%s' ,'%s ','%s') "% (id1,name,age))
        cur.execute("SELECT * FROM SUBSCRIBERS")
        for row in cur.fetchall():
            print row
    elif(ch2==2):
        n = input("enter the number of SUBSCRIBERS u want to delete :")
        i = 0
        while (i<n):
            dname = input("enter name of the SUBSCRIBER to delete")
            cur.execute("DELETE FROM SUBSCRIBERS WHERE name = '%s' "% (dname))
            i = i+1;
        cur.execute("SELECT * FROM SUBSCRIBERS")
        for row in cur.fetchall():
            print row
    elif(ch2==3):
        cur.execute("SELECT * FROM SUBSCRIBERS")
        for row in cur.fetchall():
            print row
    else:
        print ("invalid choice")
else:
    print("invalid choice")
db.commit()
db.close()
