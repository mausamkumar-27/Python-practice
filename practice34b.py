#from functools import reduce
# Raw server logs: "Timestamp | Endpoint | Status_Code | Response_Time"
server_logs = [
    "  2026-11-16 10:00:15 | /api/login | 200 | 120ms  ",
    "2026-11-16 10:01:02 | /api/checkout | 500 | 850ms",
    "  2026-11-16 10:02:40 | /api/login | 401 | 45ms ",
    "2026-11-16 10:03:10 | /api/dashboard | 200 | 310ms",
    "  2026-11-16 10:04:55 | /api/checkout | 200 | 450ms  "
]
target_statuses = {200, 401}
latency_criteria = lambda latency_ms: latency_ms > 300
key_list=["timestamp","endpoint","status","latency"]

cleaned_sl=list(map(lambda x:x.strip().split("|"),server_logs))
#print(cleaned_sl)
zip_list=list(map(lambda y:list(zip(key_list,y)),cleaned_sl))
#print(zip_list)
cleaned_dict=list(map(lambda y:dict(y),zip_list))
#print(cleaned_dict)
final_dict=list(map(lambda x:{**x,
    "timestamp":x["timestamp"].strip(),
    "endpoint":x["endpoint"].strip(),
    "status":int(x["status"].strip()),
     "latency":int(x["latency"].strip().replace("ms",""))
},cleaned_dict))
print(final_dict)