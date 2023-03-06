import pandas as pd
from dash_app.app import *


# get datasets
clean_dataset = pd.read_csv("./strava_activities.csv", delimiter=",")



# start the web app
dash_server = DashServer(
    df = clean_dataset,
    df_name = "My Activities",
    module_name=__name__

)

app = dash_server.start()
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)


