import json
import re
# x = input()
# with open("data_file.json", "w") as write_file:
#   json.dump(write_file)
#   write_file.close()
with open("data_file.json", "r") as json_file:
  data = json.load(json_file)
# data = json.loads(x)
len = len(data)
stop_name_error = 0
stop_type_error = 0
a_time_error = 0
for i in range(0, len):
  template_stop_name = r"^[A-Z].+ (Street|Avenue|Boulevard|Road)+$"
  template_stop_type = r'^[S,O,F]$|^$'
  template_a_time = r'(^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$)'
  if re.match(template_stop_name, (data[i]["stop_name"])) is None:
    stop_name_error += 1    #The stop name must end on Street, Avenue, Boulevard or Road
  if re.match(template_stop_type, (data[i]["stop_type"])) is None:
    stop_type_error += 1    #Stop_type could be: S, O, F or an empty string
  if re.match(template_a_time, (data[i]["a_time"])) is None:
    a_time_error += 1  #  Military hour goes from 00:00 to 23:59, I suggest use (element1|element2|element3) for the first cluster of hour.
sum = stop_name_error + stop_type_error + a_time_error

print(f"""Format validation: {sum} errors
stop_name: {stop_name_error}
stop_type: {stop_type_error}
a_time: {a_time_error} """)
