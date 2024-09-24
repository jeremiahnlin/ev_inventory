import panel as pn
import pandas as pd

from ..server import connection
def home_page(layout,db_value, host_value, port_value, user_value, password_value):
    pn.extension()
    elements = []
    server1 = connection(db, host, pswrd, port, user)
    server1 = connection(db_value, host_value, password_value, port_value, user_value)


    changed_layout = pn.Column(*elements)
    layout[:] = [changed_layout]
