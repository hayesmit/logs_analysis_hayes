#!/user/bin/python3

import psycopg2
DBNAME = "news"


def popular_articles():
    """display the 3 most frequently viewed articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as count "
              "from articles join log "
              "on log.path like concat('/articles/', articles.slug) "
              "group by title "
              "order by count desc "
              "limit 3;")
    posts = c.fetchall()
    print("\nThe 3 articles that have received the most views are: \n")
    for (article, views) in posts:
        print(article + " --- " + str(views) + " views")
    db.close()
    return posts


def top_authors():
    """which author has the most views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, views "
              "from authors join id_views "
              "on authors.id = id_views.id;")
    db.commit()
    posts = c.fetchall()
    print(
        "\nHere is a list of our most popular authors and how many views "
        "their articles have generated:\n")
    for (name, views) in posts:
        print("{0} --- {1}".format(str(name), str(views) + ' views'))
    db.close()
    return posts


def bad_days():
    """Reveals days in which there are more than one percent of searches
    resulting in error:"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select errors.date, errors.errors *1. / total_queries.queries "
        "as error_percent "
        "from errors join total_queries "
        "on total_queries.date = errors.date "
        "where errors.errors * 1. / total_queries.queries > 0.01;")
    posts = c.fetchall()
    print(
        "\nHere is the day that they experienced more than one percent "
        "request errors:\n")
    for (date, error_percent) in posts:
        print(str(date) + " --- " + "{0:.2%}".format(error_percent))
    db.close()
    return posts


if __name__ == '__main__':
    popular_articles()
    top_authors()
    bad_days()
