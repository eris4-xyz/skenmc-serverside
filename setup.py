import os
import mysql.connector
from mysql.connector import errorcode

import shutil

config = {
    'user': 'eris4x',
    'password': 'rexis4x@33#',
    'host': 'localhost',
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
        
    exclude_databases = ['information_schema', 'mysql', 'performance_schema', 'sys']

    for (database,) in databases:
        if database not in exclude_databases:
            try:
                cursor.execute(f"DROP DATABASE `{database}`")
                print(f"DROPPED DB: {database}")
            except mysql.connector.Error as err:
                print(f"ERR DROPPING DB {database}: {err}")
                
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS skenmc")
    print(f"DB: \"skenmc\" CREATED SUCCESSFULLY")
    
    cursor.execute("USE skenmc")

    cursor.execute("""
    CREATE TABLE all_skn (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE new (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    print("Table 'new' created successfully.")

    cursor.execute("""
    CREATE TABLE t100 (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    print("Table 't100' created successfully.")

    cursor.execute("""
    CREATE TABLE gskins (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    print("Table 'gskins' created successfully.")

    cursor.execute("""
    CREATE TABLE bskins (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    print("Table 'bskins' created successfully.")

    cursor.execute("""
    CREATE TABLE hdskins (
    sn INT AUTO_INCREMENT PRIMARY KEY,
    skn_hash VARCHAR(256) UNIQUE,
    skn_nm VARCHAR(18),
    skn_sm VARCHAR(62) UNIQUE,
    skn_qs VARCHAR(12),
    skn_uid1 VARCHAR(48) UNIQUE,
    skn_uid2 VARCHAR(48) UNIQUE,
    skn_dl INT DEFAULT 0,
    skn_vw INT DEFAULT 0
    )
    """)

    print("Table 'hdskins' created successfully.")

    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Fix User:Pass")
    else:
        print(err)

exist = os.path.exists('skenmc')

if exist:
    shutil.rmtree('skenmc')
    print("removed dir skenmc")
    os.makedirs('skenmc')
    print("recreated dir skenmc")
else:
    os.makedirs('skenmc')
    print("created dir skenmc")