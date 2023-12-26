import MySQLdb

conn = MySQLdb.connect('localhost','root','Trupti@7?','adhyayan')
curs = conn.cursor()
while True:
    ch = int(input("\n\nEnter choice.\n1.Add Student\t\t2.Show student\t\t3.Update Student\t\t4.Delete Student\t\t5.sort student\t\t6.search student\t\t7.exit"))
    match ch:
                 case 1:
                     print("add a student")
                     r = int(input("enter rn"))
                     n = int(input("enter name"))
                     m = float(input("enter mark"))
                     curs.execute((f"INSERT INTO student5 values({r},'{n}',{m}"))
                     conn.commit()
                     print("student added")
             
              
                 case 2:
                     print("show all student")
                     curs.execute("select * from student5")
                     print("rn\tname\tmarks")

                     for row in curs:
                         print(row[0],'\t',row[1],'\t',row[2])

                 case 3:
                     print("updae a student")
                     r = int(input("enter rn to update"))

                     m = int(input("enter updated marks"))
                     curs.execute(f"update student5 set marks={m} where rn={r}")
                     conn.commit()
                     print("student update")

                 case 4:
                     print("delete a student")
                     r = int(input("enter rn delete"))
                     curs.execute(f"delete from student5 where rn={r}")
                     conn.commit()
                     print("student delete")

                 case 5:
                     print("sort a studdent")
                     ch2 = int(input("1.sort by rn\t2.sort by marks\n3.sort by name"))
                     match ch2:
                         case 1:
                             print("sort by rn")
                             curs.execute("select * from student5 order by rn")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])
                         case 2:
                             print("sort by desc rn")
                             curs.execute("select * from student5 order by rn desc")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])

                         case 3:
                             print("sort by marks")
                             curs.execute("select * from student5 order by marks")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])
                         case 4:
                             print("sort by desc marks")
                             curs.execute("select * from student5 order by name")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])

                         case _:
                             print("invalid choice")
                                   
                                      

                 case 6:
                    print("search a student")
                    ch3 = int(input("1.search by rn\t2.search by name\n3.search by  marks "))
                    match ch3:
                         case 1:
                             print("search by rn to search:")
                             r = int(input("enter rn to search:"))
                             curs.execute(f"select * from student5 where rn='{r}'")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])

                         case 2:
                             print("search by name:")
                             n = input("enter name to search:")
                             curs.execute(f"select * from student5 where name='{n}'")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])

                         case 3:
                             print("search by marks:")
                             m = float(input("enter marks to search:"))
                             curs.execute(f"select * from student5 where marks='{m}'")
                             print("rn\tname\tmarks")
                             for row in curs:
                                 print(row[0],'\t',row[1],'\t',row[2])       
                 case 7:
                     print("exit")
                     break
                  

                 case _:
                     print("invalid choice")

conn.close()                      
