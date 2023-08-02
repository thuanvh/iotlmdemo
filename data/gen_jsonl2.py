
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
with open('output_2.jsonl', mode='w') as writer:
    for i in range(len(data_df)) :
        # print(type(data_df.loc[i, "volt"]))
        failure_list = [ "failure_comp" + str(j) for j in range(1,5) if label_df.loc[i, "failure_comp" + str(j)]]
        # if label_df.loc[i, "failure_comp1"] : failure_list.append("failure_comp1")
        # if label_df.loc[i, "failure_comp2"] : failure_list.append("failure_comp2")
        # if label_df.loc[i, "failure_comp3"] : failure_list.append("failure_comp3")
        # if label_df.loc[i, "failure_comp4"] : failure_list.append("failure_comp4")

        main_list = [ "maint_comp" + str(j) for j in range(1,5) if label_df.loc[i, "maint_comp" + str(j)]]
        # if label_df.loc[i, "maint_comp1"] : main_list.append("maint_comp1")
        # if label_df.loc[i, "maint_comp2"] : main_list.append("maint_comp2")
        # if label_df.loc[i, "maint_comp3"] : main_list.append("maint_comp3")
        # if label_df.loc[i, "maint_comp4"] : main_list.append("maint_comp4")

        # main_list = []
        # if label_df.loc[i, "maint_comp1"] : failure_list.append("maint_comp1")
        # if label_df.loc[i, "maint_comp2"] : failure_list.append("maint_comp2")
        # if label_df.loc[i, "maint_comp3"] : failure_list.append("maint_comp3")
        # if label_df.loc[i, "maint_comp4"] : failure_list.append("maint_comp4")

        error_list = [ "error" + str(j) for j in range(1,6) if label_df.loc[i, "error" + str(j)]]
        # if label_df.loc[i, "error1"] : error_list.append("error1")
        # if label_df.loc[i, "error2"] : error_list.append("error2")
        # if label_df.loc[i, "error3"] : error_list.append("error3")
        # if label_df.loc[i, "error4"] : error_list.append("error4")
        # if label_df.loc[i, "error5"] : error_list.append("error5")

        writer.write(json.dumps({"id":i,"volt": data_df.loc[i, "volt"],
                      "rotate": data_df.loc[i, "rotate"],
                      "pressure": data_df.loc[i, "pressure"],
                      "vibration": data_df.loc[i, "vibration"],
                      "age": data_df.loc[i, "age"],
                      "anomaly": data_df.loc[i, "anomaly"],
                      "failure_list": failure_list,
                      "main_comp_list": main_list,
                      "error_list": error_list,
                      "failure": label_df.loc[i, "failure"],
                      "maint": label_df.loc[i, "maint"],
                      "error": label_df.loc[i, "error"]
                      }, cls = MyEncoder))
        writer.write("\n")

