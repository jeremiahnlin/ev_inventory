import pymysql


# Connecting to database, host, pass, and user all vary
    # Please insert HOST, PASSWORD, and USER

def connection():
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-2332b00d-inventory-system.k.aivencloud.com",                                      
        password="AVNS_VN-gN724glxc0oBiNgJ",                                  
        read_timeout=timeout,
        port=28334,
        user="avnadmin",                                      
    )
    try:
        cursor = connection.cursor()
    except:
        print("Connection Rejected")
        
    return connection
