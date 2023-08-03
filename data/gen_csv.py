
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as parquet
import pyarrow.feather as feather
import jsonlines
import numpy as np
import json
file_data = "pmfpdata/iot_pmfp_data.feather"
file_label = "pmfpdata/iot_pmfp_labels.feather"
data_df = feather.read_feather(file_data)
print(data_df.columns)
# print(type(data_df))
print(data_df)

label_df = feather.read_feather(file_label)
print(label_df)
print(label_df.columns)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

# with jsonlines.open('output.jsonl', mode='w') as writer:
print(len(data_df))
with open('output.csv', mode='w') as writer:
    writer.write("id,volt,rotate,pressure,vibration,age,anomaly,failure_comp1,failure_comp2,failure_comp3,failure_comp4,maint_comp1,maint_comp2,maint_comp3,maint_comp4,error1,error2,error3,error4,error5,failure,maint,error\n")
    for i in range(len(data_df)) :

        # print(type(data_df.loc[i, "volt"]))
        writer.write(str(i) + ","+str( data_df.loc[i, "volt"]) 
                      +","+str( data_df.loc[i, "rotate"])
                      +","+str( data_df.loc[i, "pressure"])
                      +","+str( data_df.loc[i, "vibration"])
                      +","+str( data_df.loc[i, "age"])
                      +","+str( data_df.loc[i, "anomaly"])
                      +","+str( label_df.loc[i, "failure_comp1"])
                      +","+str( label_df.loc[i, "failure_comp2"])
                      +","+str( label_df.loc[i, "failure_comp3"])
                      +","+str( label_df.loc[i, "failure_comp4"])
                      +","+str( label_df.loc[i, "maint_comp1"])
                      +","+str( label_df.loc[i, "maint_comp2"])
                      +","+str( label_df.loc[i, "maint_comp3"])
                      +","+str( label_df.loc[i, "maint_comp4"])
                      +","+str( label_df.loc[i, "error1"])
                      +","+str( label_df.loc[i, "error2"])
                      +","+str( label_df.loc[i, "error3"])
                      +","+str( label_df.loc[i, "error4"])
                      +","+str( label_df.loc[i, "error5"])
                      +","+str( label_df.loc[i, "failure"])
                      +","+str( label_df.loc[i, "maint"])
                      +","+str( label_df.loc[i, "error"])
                      )
        writer.write("\n")

