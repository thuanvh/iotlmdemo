
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as parquet
import pyarrow.feather as feather
from ydata_profiling import ProfileReport

file_data = "pmfpdata/iot_pmfp_data.feather"
file_label = "pmfpdata/iot_pmfp_labels.feather"
data_df = feather.read_feather(file_data)

# print(type(data_df))
# print(data_df)

label_df = feather.read_feather(file_label)
# print(label_df)

print(data_df.info())
print(data_df.describe())

profile = ProfileReport(data_df, title="Profiling Report")
profile.config.html.inline = True

profile.to_file("your_report.html")

# json_data = profile.to_json()
# profile.to_file("your_report.json")
 
# profile.to_file("your_report.pdf")
# # site = df[df["Site Num"] == 3003]
# type_schema = {
#     "datetime": "timeseries"
# }
# profilets = ProfileReport(data_df, tsmode=True, type_schema=type_schema, sortby="datetime", title="Time-Series EDA")

# profilets.to_file("report_timeseries.html")
