import pandas as pd
from dash_app.app import *


# get datasets
dataset = pd.read_csv("test_data.csv", delimiter=",")



# start the web app
dash_server = DashServer(
    df = dataset,
    df_name = "My Activities",
    module_name=__name__

)

app = dash_server.start()
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)


