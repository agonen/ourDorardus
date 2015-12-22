import psycopg2,requests
from psycopg2.extras import NamedTupleCursor


# get data in string from
for k in psycopg2.extensions.string_types.keys():
    del psycopg2.extensions.string_types[k]

conn = psycopg2.connect(dsn="dbname=merit user=gpadmin password=changeme host=10.169.54.35",cursor_factory=NamedTupleCursor)
cur = conn.cursor()
cur.execute("select alert_id,alert_start_time,delivery_method,destination_email from dbo.alerts;")
a = cur.fetchall()
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
    # j["doc"]["destination_ip"] = i.destination_ip
    # j["doc"]["destination_port"] = i.destination_port
    # j["doc"]["file_mime_type"] = i.file_mime_type
    # j["doc"]["file_name"] = i.file_name
    # j["doc"]["hash_id"] = i.hash_id
    # j["doc"]["co_id_server"] = i.co_id_server
    # j["doc"]["co_id_client"] = i.co_id_client
    # j["doc"]["source_ip"] = i.source_ip
    # j["doc"]["source_port"] = i.source_port
    # j["doc"]["correlation_id"] = i.correlation_id
    # j["doc"]["ipgl_client_region"] = i.ipgl_client_region
    # j["doc"]["ipgl_client_longitude"] = i.ipgl_client_longitude
    # j["doc"]["ipgl_client_latitude"] = i.ipgl_client_latitude
    # j["doc"]["ipgl_client_autonomous_system_number"] = i.ipgl_client_autonomous_system_number
    # j["doc"]["ipgl_client_autonomous_system_name"] = i.ipgl_client_autonomous_system_name
    # j["doc"]["ipgl_server_country"] = i.ipgl_server_country
    # j["doc"]["ipgl_server_region"] = i.ipgl_server_region
    # j["doc"]["ipgl_server_city"] = i.ipgl_server_city
    # j["doc"]["ipgl_server_postal_code"] = i.ipgl_server_postal_code
    # j["doc"]["ipgl_server_longitude"] = i.ipgl_server_longitude
    # j["doc"]["ipgl_server_latitude"] = i.ipgl_server_latitude
    # j["doc"]["ipgl_server_isp_name"] = i.ipgl_server_isp_name
    # j["doc"]["ipgl_server_organization_name"] = i.ipgl_server_organization_name
    # j["doc"]["ipgl_server_autonomous_system_number"] = i.ipgl_server_autonomous_system_number
    # j["doc"]["ipgl_server_autonomous_system_name"] = i.ipgl_server_autonomous_system_name
    # j["doc"]["url_categorization"] =  i.url_categorization


    insert_list.append(j)
batch_cmd = {"batch" : {"docs": insert_list}}

#print batch_cmd

#resp = requests.get(url='http://10.61.40.33:1123/email/Person/_aggregate?range=*&m=COUNT(LastName)&f=FirstName',headers={'Content-Type': 'application/json'})
#print batch_cmd
resp = requests.post(url='http://10.61.40.33:1123/TTLP/shard1',headers={'Content-Type': 'application/json'},json=batch_cmd)
#print batch_cmd
print resp.raise_for_status()
#if resp.status_code != 200:
    # This means something went wrong.
#    raise ApiError('GET  {}'.format(resp.status_code))

#print resp.json()
