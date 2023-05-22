import pandas as pd
from sqlalchemy import create_engine

import urllib.parse


connection_string = 'mysql://username:pass@localhost:3306/excel'


parsed = urllib.parse.urlparse(connection_string)
new_password = urllib.parse.quote(parsed.password)


updated_connection_string = connection_string.replace(parsed.password, new_password)



df = pd.read_excel('excel.xlsx')
print(df)
engine = create_engine(updated_connection_string)
df.to_sql('peoplebro', con=engine, if_exists='append')