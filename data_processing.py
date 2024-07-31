import pandas as pd
import os

def processData():
  output_file_path = os.path.abspath('data/output.csv')

  # remove existing file
  if os.path.isfile(output_file_path):
    os.remove(output_file_path)

  df_list = []
  for filename in os.listdir('./data'):
    file_path = os.path.abspath(f'data/{filename}')
    df = pd.read_csv(file_path, low_memory=False)

    df = df.loc[df['product'] == "pink morsel", :]

    # convert price to numerical and compute sales
    df['price'] = df.price.str.lstrip('$').astype(float)
    df['sales'] = df.price * df.quantity

    df = df[['sales', 'date', 'region']].rename(columns={
      'sales': 'Sales',
      'date': 'Date',
      'region': 'Region'
    })

    df_list.append(df)

  output_df = pd.concat(df_list)
  output_df.to_csv(output_file_path, index=False)

if __name__=="__main__":
  output_df = processData()
