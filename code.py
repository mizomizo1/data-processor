from google.colab import drive
import pandas as pd
import numpy as np
import warnings

class DataProcessor:
    def __init__(self, data_path, submit_path):
        drive.mount('/content/drive')
        warnings.filterwarnings('ignore')
        self.df = pd.read_csv(data_path)
        self.df_submit = pd.read_csv(submit_path)
        self.preprocess_data()

    def preprocess_data(self):
        # 重複していないidの行を取得
        unique_df = self.df[~self.df.duplicated(subset=['id'], keep=False)]

        # 重複するidを持つ行を抽出
        duplicate_ids = self.df[self.df.duplicated(subset=['id'], keep=False)]

        # idごとに最新の時間を取得
        latest_times = duplicate_ids.loc[duplicate_ids.groupby('id')['time'].idxmax()]

        # 重複していないデータと最新のデータ結合
        self.df = pd.concat([unique_df, latest_times])

        # 'id'列でソート
        self.df = self.df.sort_values('id')

        # Create a dictionary where keys are 'id' and values are 'name' from the dataframe.
        self.id_name_dict = dict(zip(self.df_submit['id'], self.df_submit['name']))
        self.update_submit_data()

    def update_submit_data(self):
      for index, row in self.df_submit.iterrows():
          student_id = row['id']

          # Check if the 'id' exists in df and id_name_dict
          if student_id in self.id_name_dict and student_id in self.df['id'].values:
              # Find the corresponding row in df
              df_row = self.df[self.df['id'] == student_id]

              # Update NG_1 and NG_2 in df_submit if they exist in df
              if 'NG_1' in df_row.columns and not pd.isna(df_row['NG_1'].iloc[0]):
                  self.df_submit.loc[index, 'NG_1'] = df_row['NG_1'].iloc[0]
              if 'NG_2' in df_row.columns and not pd.isna(df_row['NG_2'].iloc[0]):
                  self.df_submit.loc[index, 'NG_2'] = df_row['NG_2'].iloc[0]
      
    def get_processed_data(self):
        return self.df, self.df_submit

"""
df
<class 'pandas.core.frame.DataFrame'>
Index: 124 entries, 0 to 127
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   time    124 non-null    object 
 1   id      124 non-null    int64  
 2   name    124 non-null    object 
 3   NG_1    122 non-null    float64
 4   NG_2    122 non-null    float64
dtypes: float64(2), int64(1), object(2)
memory usage: 5.8+ KB
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 127 entries, 0 to 126

df_submit
Data columns (total 10 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   id                            127 non-null    int64  
 1   name                          127 non-null    object 
 2   furigana                      127 non-null    object 
 3   sex (man=" 1 ", woman=" 0 ")  127 non-null    int64 
 4   NG_1                          122 non-null    float64
 5   NG_2                          122 non-null    float64
 6   NG_3                          0 non-null      float64
 7   NG_4                          0 non-null      float64
 8   NG_5                          0 non-null      float64
dtypes: float64(5), int64(2), object(3)
memory usage: 10.0+ KB
"""
