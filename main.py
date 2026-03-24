from database.dbconn import dbInit, sqlExecute
from ai_agent import text_to_sql


def main():
    dbInit()

    text = input()

    sql = text_to_sql(text)
    print(sql)
    answer = sqlExecute(sql)


if __name__=="__main__":
    main()
