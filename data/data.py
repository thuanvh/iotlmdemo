
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as parquet
import pyarrow.feather as feather

file_data = "pmfpdata/iot_pmfp_data.feather"
file_label = "pmfpdata/iot_pmfp_labels.feather"
data_df = feather.read_feather(file_data)

print(type(data_df))
print(data_df)

label_df = feather.read_feather(file_label)
print(label_df)
