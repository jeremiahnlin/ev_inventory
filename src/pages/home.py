import panel as pn
import pandas as pd
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
sys.path.append(script_dir)

from server import connection

def home_page(layout,db_value, host_value, port_value, user_value, password_value):
    pn.extension()
    elements = []
    server1 = connection(db_value, host_value, password_value, port_value, user_value)
    

    changed_layout = pn.Column(*elements)
    layout[:] = [changed_layout]
