#!/usr/bin/env python
import snowflake.connector
import configparser

config = configparser.ConfigParser()
config.read('/home/apizarro/Desarrollo/Personal_Code/Learn_Python/Snowflake_Curso_Basico/config.ini')

# Gets the version
ctx = snowflake.connector.connect(
    user = config.get('varlogin','user'),
    password = config.get('varlogin','password'),
    account = config.get('varlogin','account')
    #PASSWORD = os.getenv('SNOWSQL_PWD') - En caso se utilice variable de entorno
    #You can set session parameters to tweak your session and have it set up just the way you want it.
    #you can set them when you initially connect, like so:
    #session_parameters={
        #'QUERY_TAG': 'EndOfMonthFinancials',
    #}
    #you can set them after you connect by executing the SQL statement ALTER SESSION SET:
    #conn.cursor().execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")
    )
cs = ctx.cursor()
try:
    #Se obtiene la version de Snowflake
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
    #Se crea un warehouse llamado tiny_warehouse_mg de tamaño 'X-SMALL' 
    cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg \
        with warehouse_size='X-SMALL' auto_suspend = 180 \
        auto_resume = true initially_suspended=true;")
    ctx.commit
    #Se usa el warehouse creado
    cs.execute("USE WAREHOUSE tiny_warehouse_mg")
    #Se crea un database llamado testdb 
    cs.execute("CREATE DATABASE IF NOT EXISTS testdb")
    ctx.commit
    #Se usa el database creado
    cs.execute("USE DATABASE testdb")
    #Se crea un database llamado testdb 
    cs.execute("CREATE SCHEMA IF NOT EXISTS testschema")
    ctx.commit
    #Se usa el database creado
    cs.execute("USE SCHEMA testschema")
    #Se valida el uso de los objetos creados
    cs.execute("select CURRENT_WAREHOUSE(), current_database(), current_schema()")
    datawarehouse = cs.fetchone()
    print("El warehouse usado es: ", datawarehouse[0])
    print("El database usado es: ", datawarehouse[1])
    print("El schema usado es: ", datawarehouse[2])
finally:
    cs.close()
ctx.close()
