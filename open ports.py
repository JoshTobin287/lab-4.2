import json  

with open("scan_results.json", "r") as file:
    data = json.load(file)  

open_ports = []

for result in data["results"]:
    if result["open"]:           
        open_ports.append(result["port"])  

print("Number of open ports:", len(open_ports))
print("Open ports are:", open_ports)
