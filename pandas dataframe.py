import pandas as pd

df = pd.read_html('https://www.premierleague.com')
print(df[0])
