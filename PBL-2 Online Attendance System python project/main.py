import subprocess
scan_results = subprocess.check_output(["netsh", "wlan", "show", "network"])
scan_results = scan_results.decode("ascii")
scan_results = scan_results.replace("\r","")
lst = scan_results.split("\n")
lst = lst[4:]

str = ["38 Chetan Kasar", "22 Pranav Gadakh", "31 Milind Ghegadmal","23 Pratik Gadekar","34 roop" , "27 Maitreya Gangurde", "26 sanket kale","prajwal"]
present = []
absent = []
wifi_names = []
set =0

if len(lst)>0:
    for eachItem in lst:
        if eachItem[0:4] == "SSID":
            SSID_cleared = eachItem[eachItem.find(":")+2:]
            for names in str:
                if names == SSID_cleared:
                    wifi_names.append(SSID_cleared)

for i in str:
  for ele in wifi_names:
    if i == ele:
      present.append(i)
      set = 1
  if set == 0:
    absent.append(i)
  else:
    set = 0                   

print("\nPresent students list : \n")
for j in present:
  print(j)   

print("\nAbsent student : \n")
for k in absent:
  print(k)

print("\n")
