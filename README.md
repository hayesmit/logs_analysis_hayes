# Project: Log Analysis

## FUCTION:
mitchell_hayes_project_one.py program has been designed to to perform 3 queries
to a news sites database. The first query will find the three most frequently
visited articles. The second query will rank the authors according to to how
many times they have had someone request one of their articles.The third query
will display which days there were more than one percent request errors.

## WHY:
We have been asked to practice our sql skills in a real world scenario,
extracting data in an attempt to make better decisions on the types of articles
people want to read, which authors are most read and pinpointing ways to make
our readers experience better by finding errors.

## INSTALATION:
In order to run this code you will need to be in your
[vagrant virtual machine](https://www.vagrantup.com/docs/virtualbox/), and have
in the current working directory both the newsdata.sql file and the
mitchell_hayes_project_one.py file. Create the news database by running
`$ psql -d news -f newsdata.sql` in the virtual machine
command line. this creates a news database with three tables in it titled
articles, log and authors. my code requires the addition of three views. Which
can be created after gaining access to the news database by entering
`psql news` in the command line.

###view entry one:
`$ create or replace view id_views as
select articles.author as id, count(*) as views
from articles join log on log.path like concat('/article/', articles.slug)
group by articles.author
order by views desc;`
-2 columns: column one is the authors id number
            column two is the number visitors each author had

###view entry two:
`create or replace view total_queries as
select time::timestamp::date as date, count(*) as queries
from log
group by time::timestamp::date
order by date;`
-2 columns: column one date
            column two total number of queries on the particular date

###view entry three:
`create or replace view errors as
select time::timestamp::date as date, count(*) as errors
from log
where status != '200 OK'
group by time::timestamp::date
order by date;`
-2 columns: column one date
            column two the number of errors on the particular date.

### license:
This is a for a class project. Feel free to do whatever you would like with it.
