import os
import warnings

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


class DashServer:
    """
    Class for setting up and running the Dash Server

    :param df: the dataset with all the activities by the athlete
    :param df_name: name of the dataset in the dashboard

    """

    def __init__(self,
            df: pd.DataFrame,
            df_name: str, module_name
    ) -> object:
        self.df = df
        self.df_name = df_name
        self.module_name = module_name

    def start(self):

        assets_path = os.getcwd() + "/assets"
        app = Dash(self.module_name, assets_folder = assets_path)

        df = self.df

        activity_type = df.type.value_counts()
        fig = px.bar(activity_type)

        app.layout = html.Div(children=[

            html.H1('Hello World'),

            html.Div(children='''
                WEB UNDER CONSTRUCTION - STRAVA DATA SOON....
            '''),

            dcc.Graph(
                id = 'example-graph',
                figure = fig
            )
        ])


        return app 





        

        