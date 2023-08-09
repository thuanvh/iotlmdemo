
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as parquet
import pyarrow.feather as feather
import jsonlines
import numpy as np
import json
import pandas as pd
file_data = "pmfpdata/iot_pmfp_data.feather"
file_label = "pmfpdata/iot_pmfp_labels.feather"
data_df = feather.read_feather(file_data)
print(data_df.columns)
# print(type(data_df))
print(data_df)

label_df = feather.read_feather(file_label)
print(label_df)
print(label_df.iloc[:,2:-1])
print(label_df.iloc[:,2:-1].columns)
# label_df.rename(columns = {'anomaly':'anomaly_label'}, inplace = True)

df3 = pd.concat([data_df, label_df.iloc[:,2:-1]],axis=1, ignore_index=False, sort=False)
print(df3)
# pd.merge(data_df, restaurant_review_frame, on='business_id', how='outer')
feather.write_feather(df3, 'pmfpdata/iot_pmfp_merged.feather')