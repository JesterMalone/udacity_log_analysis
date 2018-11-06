#!/usr/bin/env python3
# Logs Analysis

from loganalysisdb import get_db_connection, get_top_articles, \
  get_top_authors, get_top_errors
from datetime import datetime


def print_top_articles(db_cursor):
    results = get_top_articles(db_cursor)

    print("====Top three articles====")
    for result in results:
        print('{title} - {count} views'.format(
          title=result[0], count=result[1]))


def print_top_authors(db_cursor):
    results = get_top_authors(db_cursor)

    print("====Top Authors====")
    for result in results:
        print('{author} - {count} views'.format(
          author=result[0], count=result[1]))


def print_top_errors(db_cursor):
    results = get_top_errors(db_cursor)

    print("====Top Errors Per Day====")
    for result in results:
        print('{date} - {error_rate}''%'' errors'.format(
          date=result[0], error_rate=result[1]))


if __name__ == "__main__":
    CURSOR = get_db_connection()
    if CURSOR:
        print_top_articles(CURSOR)
        print
        print_top_authors(CURSOR)
        print
        print_top_errors(CURSOR)
        CURSOR.close()
