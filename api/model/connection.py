from model.DBConnection import DBConnection

connection = None

def init_connection(settings):
    connection = DBConnection()
    connection.connect(settings)
