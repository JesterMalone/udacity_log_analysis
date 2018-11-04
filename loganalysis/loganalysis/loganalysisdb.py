# "Database code" for the news database.
import psycopg2


DBNAME = "news"


def get_db_connection():
    dbConnect = psycopg2.connect(database=DBNAME)
    db_cursor = dbConnect.cursor()
    return db_cursor


def get_top_articles(db_cursor):
    """Return top three articles and total views, in descending order:"""
    query = '''
      SELECT CONCAT('"', articles.title, '"') as Title
          ,COUNT(log.path) AS totalViews
      FROM articles
      JOIN log on articles.slug = substr(log.path, length('/article/') + 1)
      GROUP BY
        articles.slug
        ,articles.title
      ORDER BY totalViews DESC
      LIMIT 3;
      '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    return results


def get_top_authors(db_cursor):
    """Return top authors and total views, in descending order:"""
    query = '''
    SELECT
        authors.name
        ,COUNT(authors.id) AS totalViews
    FROM authors
    JOIN articles  ON authors.id = articles.author
    JOIN log ON articles.slug = SUBSTR(log.path, length('/article/') + 1)
    GROUP BY
        authors.name
        ,authors.id
    ORDER BY totalViews DESC;
    '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    return results


def get_top_errors(db_cursor):
    """Return top errors:"""
    query = '''
    SELECT
        to_char(day, 'MON DD, YYYY') AS datetime
        ,ROUND(errorpercent::numeric,1)
    FROM error_rate WHERE errorPercent > 1;
    '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    return results
