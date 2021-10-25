import pandas as pd
import plotly.express as px

df = pd.read_csv("./CovidData.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "Covid Cases of different countries")
fig.show()