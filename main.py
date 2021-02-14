import json
# x = input()
# with open("data_file.json", "w") as write_file:
#   json.dump(write_file)
#   write_file.close()
with open("data_file.json", "r") as json_file:
  data = json.load(json_file)
# data = json.loads(x)
len = len(data)
bus_error = 0
stop_id_error = 0
stop_name_error = 0
next_stop_error = 0
stop_type_error = 0
a_time_error = 0
for i in range(0, len):
  if type(data[i]["bus_id"]) is not int:
    bus_error += 1
  if type(data[i]["stop_id"]) is not int:
    stop_id_error += 1
  if type(data[i]["stop_name"]) is not str or data[i]["stop_name"] == "":
    stop_name_error += 1  # here is not vsalid
  if type(data[i]["next_stop"]) is not int:
    next_stop_error += 1
  if type(data[i]["stop_type"]) is not str or data[i]["stop_type"] != 'F' and data[i]["stop_type"] != 'S' and data[i]["stop_type"] != 'O' and data[i]["stop_type"] != '':
    stop_type_error += 1
  if type(data[i]["a_time"]) is not str or data[i]["a_time"] == "":
    a_time_error += 1
sum = bus_error + stop_id_error + stop_name_error + next_stop_error + stop_type_error + a_time_error

print(f"""Type and required field validation: {sum} errors
bus_id: {bus_error}
stop_id: {stop_id_error}
stop_name: {stop_name_error}
next_stop: {next_stop_error}
stop_type: {stop_type_error}
a_time: {a_time_error}""")