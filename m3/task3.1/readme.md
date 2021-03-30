## Module 3 Database Administration
## TASK 3.1

Task 1-3:

Draft of my Database:

/ 1-st table: consumer ->
2-d table: datacenter ->
3-d table: availaibility-zone /

![Image description](./img/vm/scheme.png)

Task 4: Created db

![Image description](./img/vm/my_data.png)

Task 5-6:
Select, where, group by, order by:

![Image description](./img/vm/selection.png)

![Image description](./img/vm/where.png)

![Image description](./img/vm/group_by.png)

![Image description](./img/vm/order_by.png)

Task 7.Execute other different SQL queries DDL, DML, DCL.

## DDl:

select:
![Image description](./img/vm/1.png)

alter:

![Image description](./img/vm/2.png)

drop:    
![Image description](./img/vm/3.png)

comment and rename:
![Image description](./img/vm/4.png)

## DML:

insert:

![Image description](./img/vm/5.png)

update:   
![Image description](./img/vm/6.png)

delete:  
![Image description](./img/vm/7.png)

Result of merging between two tables:

![Image description](./img/vm/merge.png)

call:    
![Image description](./img/vm/8.png)

explain:  
![Image description](./img/vm/9.png)

update:

![Image description](./img/vm/10.png)

## DСL:

grant:

![Image description](./img/vm/11.png)

revoke:  
![Image description](./img/vm/12.png)

## Part 2

Task 10-12: backup of db and dropping one ttable

![Image description](./img/part2/datacenter_tables.png)

For backup I used cmd: mysqldump -uroot -h 127.0.0.1 -p datacenter > backup.sql

Next screen displays restored database from file backup.SQL

![Image description](./img/part2/restored_backup.png)

As we see here all tables

Task 13-15 connect via rds:

Preparation rds:

![Image description](./img/part2/1.png)

![Image description](./img/part2/2.png)

I copied from host to aws instance backup.sgl, then via instance I connected our db from aws:

![Image description](./img/part2/3.png)

select check:
![Image description](./img/part2/4.png)

Task 16: make mysqldump

![Image description](./img/part2/5.png)

## Part 3

Task 17-19: DynamoDb

![Image description](./img/part3/1.png)

table:

![Image description](./img/part3/2.png)

![Image description](./img/part3/3.png)

scan:
![Image description](./img/part3/4.png)

query:
![Image description](./img/part3/5.png)
