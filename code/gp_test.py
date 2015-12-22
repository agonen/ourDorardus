import psycopg2,requests
from psycopg2.extras import NamedTupleCursor


# get data in string from
for k in psycopg2.extensions.string_types.keys():
    del psycopg2.extensions.string_types[k]

conn = psycopg2.connect(dsn="dbname=merit user=gpadmin password=changeme host=10.168.251.134",cursor_factory=NamedTupleCursor)
cur = conn.cursor()
cur.execute("select alert_id,alert_start_time,delivery_method,destination_email,source_ip from dbo.alerts limit 10000000;")

batch_size=10000
#a = cur.fetchall()
a = cur.fetchmany(batch_size)
while a is not None:
    insert_list = []
    j={"doc": {"_table": "Alerts"}}
    for i in a:
        j["doc"]["alert_id"]= i.alert_id
        if i.alert_start_time is not None:
          j["doc"]["alert_start_time"] = i.alert_start_time
        if i.delivery_method is not None:
          j["doc"]["delivery_method"] = i.delivery_method
        if i.destination_email is not None:
          j["doc"]["destination_email"] = i.destination_email
        if i.source_ip is not None:
          j["doc"]["source_ip"] = i.source_ip

        insert_list.append(j)
    batch_cmd = {"batch" : {"docs": insert_list}}

    resp = requests.post(url='http://10.61.40.33:1123/TTLP/shard2',headers={'Content-Type': 'application/json'},json=batch_cmd)
    resp = requests.post(url='http://10.61.40.33:1123/TTLP/shard2',headers={'Content-Type': 'application/json'},json=batch_cmd)
    print resp.raise_for_status()
    a = cur.fetchmany(batch_size)

