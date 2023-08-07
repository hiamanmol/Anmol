"""
 SQL

-> create database(name);
-> show databases;
-> use name;
-> show tables;

 Create table Customer(
      cid int primary key auto_increment,
      name text,
      phone text,
      email text
      );

      show tables;

      describe Customer;
      insert into Customer values(null,'anmol','84377 27797','anmol@gmail.com');
      select * from customer;
"""
import mysql.connector as db

class Customer:

    def __init__(self):

        self.name = input("Enter the name of the customer:")
        self.phone_no = input("Enter the phone no of the customer:")
        self.email = input("Enter the email of the customer:")

def main():

    customer = Customer()
    print(vars(customer))

    # DATABASE CONNECTIVITY

    # STEP 1-> create connection with database
    connection = db.connect(user='root',
                            password='anmolrocks@1',
                            host='127.0.0.1',
                            database='customer')

    # STEP 2-> obtain cursor to perform sql operations
    cursor = connection.cursor()

    # STEP 3-> create SQL statement
    sql = "insert into Customer values(null,'{name}','{phone_no}','{email}');".format_map(vars(customer))

    # STEP 4-> execute SQL commands
    cursor.execute(sql)
    connection.commit()

    print("customer inserted.....")

if __name__ == '__main__':
    main()