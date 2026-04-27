import psycopg2
def main():
    conn = psycopg2.connect(database="mariadb_yri6",
                            user="mariadb_yri6_user",
                            password="J8sL1alyOxScUoV4rUOpYChvkwG2ZDSt",
                            host="dpg-d7ng3t6gvqtc73ar4g00-a.frankfurt-postgres.render.com",
                            port=5432)
    
    print("DATABASE CONNECTED!")
