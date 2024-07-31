import pandas as pd
import os

def processData():
  df_list = []
  for filename in os.listdir('./data'):
    file_path = os.path.abspath(f'data/{filename}')
    df = pd.read_csv(file_path)
    df_list.append(df)

  output_df = pd.concat(df_list)
  output_df.to_csv(os.path.abspath('data/output.csv'))

if __name__=="__main__":
  output_df = processData()
