#pip install html5lib
#pip3 install lxml

import pandas as pd

df = pd.read_html('https://www.premierleague.com')
print(df[0])
