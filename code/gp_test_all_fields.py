import psycopg2,requests,time
from psycopg2.extras import NamedTupleCursor

gp_host ="10.168.251.134"


# get data in string from
for k in psycopg2.extensions.string_types.keys():
    del psycopg2.extensions.string_types[k]

batch_size=20000
conn = psycopg2.connect(dsn="dbname=merit user=gpadmin password=changeme host="+gp_host,cursor_factory=NamedTupleCursor)
cur = conn.cursor("dordauscursor")
cur.itersize=batch_size
cur.execute("select alert_id, alert_start_time, insert_time, attack_name, attack_status, bandwidth, class_type, context, delivery_method, destination_email, destination_ip, destination_ip6, destination_port, file_mime_type, file_name, hash_id, packet_count, policy_name, protocol, reference_cve, risk, sid, sid_rev, source_email, source_ip, source_ip6, source_port, alert_type, bl_direction, category, co_id, confidence, device_ip, device_name, malware_name, blocking_status, raw_index, correlation_id, co_id_server, co_id_client, destination_host, machine_id, details, description, site_id, ipgl_client_country, ipgl_client_region, ipgl_client_city, ipgl_client_postal_code, ipgl_client_longitude, ipgl_client_latitude, ipgl_client_isp_name, ipgl_client_organization_name, ipgl_client_autonomous_system_number, ipgl_client_autonomous_system_name, ipgl_server_country, ipgl_server_region, ipgl_server_city, ipgl_server_postal_code, ipgl_server_longitude, ipgl_server_latitude, ipgl_server_isp_name, ipgl_server_organization_name, ipgl_server_autonomous_system_number, ipgl_server_autonomous_system_name from dbo.alerts;")


print "copy from {0} batch size {1}".format(gp_host,batch_size)
flash = 0
index = 0
for i in cur:
    index +=1
    flash +=1
    insert_list = []
    j={"doc": {"_table": "Alerts"}}
    j["doc"]["alert_id"]= i.alert_id
    if i.alert_start_time is not None:
      j["doc"]["alert_start_time"] = i.alert_start_time
    if i.insert_time is not None:
      j["doc"]["insert_time"] = i.insert_time
    if i.attack_name is not None:
      j["doc"]["attack_name"] = i.attack_name
    if i.attack_status is not None:
      j["doc"]["attack_status"] = i.attack_status
    if i.bandwidth is not None:
      j["doc"]["bandwidth"] = i.bandwidth
    if i.class_type is not None:
      j["doc"]["class_type"] = i.class_type
    if i.context is not None:
      j["doc"]["context"] = i.context
    if i.delivery_method is not None:
      j["doc"]["delivery_method"] = i.delivery_method
    if i.destination_email is not None:
      j["doc"]["destination_email"] = i.destination_email
    if i.destination_ip is not None:
      j["doc"]["destination_ip"] = i.destination_ip
    if i.destination_ip6 is not None:
      j["doc"]["destination_ip6"] = i.destination_ip6
    if i.destination_port is not None:
      j["doc"]["destination_port"] = i.destination_port
    if i.file_mime_type is not None:
      j["doc"]["file_mime_type"] = i.file_mime_type
    if i.file_name is not None:
      j["doc"]["file_name"] = i.file_name
    if i.hash_id is not None:
      j["doc"]["hash_id"] = i.hash_id
    if i.packet_count is not None:
      j["doc"]["packet_count"] = i.packet_count
    if i.policy_name is not None:
      j["doc"]["policy_name"] = i.policy_name
    if i.protocol is not None:
      j["doc"]["protocol"] = i.protocol
    if i.reference_cve is not None:
      j["doc"]["reference_cve"] = i.reference_cve
    if i.risk is not None:
      j["doc"]["risk"] = i.risk
    if i.sid is not None:
      j["doc"]["sid"] = i.sid
    if i.sid_rev is not None:
      j["doc"]["sid_rev"] = i.sid_rev
    if i.source_email is not None:
      j["doc"]["source_email"] = i.source_email
    if i.source_ip is not None:
      j["doc"]["source_ip"] = i.source_ip
    if i.source_ip6 is not None:
      j["doc"]["source_ip6"] = i.source_ip6
    if i.source_port is not None:
      j["doc"]["source_port"] = i.source_port
    if i.alert_type is not None:
      j["doc"]["alert_type"] = i.alert_type
    if i.bl_direction is not None:
      j["doc"]["bl_direction"] = i.bl_direction
    if i.category is not None:
      j["doc"]["category"] = i.category
    if i.co_id is not None:
      j["doc"]["co_id"] = i.co_id
    if i.confidence is not None:
      j["doc"]["confidence"] = i.confidence
    if i.device_ip is not None:
      j["doc"]["device_ip"] = i.device_ip
    if i.device_name is not None:
      j["doc"]["device_name"] = i.device_name
    if i.malware_name is not None:
      j["doc"]["malware_name"] = i.malware_name
    if i.blocking_status is not None:
      j["doc"]["blocking_status"] = i.blocking_status
    if i.raw_index is not None:
      j["doc"]["raw_index"] = i.raw_index
    if i.correlation_id is not None:
      j["doc"]["correlation_id"] = i.correlation_id
    if i.co_id_server is not None:
      j["doc"]["co_id_server"] = i.co_id_server
    if i.co_id_client is not None:
      j["doc"]["co_id_client"] = i.co_id_client
    if i.destination_host is not None:
      j["doc"]["destination_host"] = i.destination_host
    if i.machine_id is not None:
      j["doc"]["machine_id"] = i.machine_id
    if i.details is not None:
      j["doc"]["details"] = i.details
    if i.description is not None:
      j["doc"]["description"] = i.description
    if i.site_id is not None:
      j["doc"]["site_id"] = i.site_id
    if i.ipgl_client_country is not None:
      j["doc"]["ipgl_client_country"] = i.ipgl_client_country
    if i.ipgl_client_region is not None:
      j["doc"]["ipgl_client_region"] = i.ipgl_client_region
    if i.ipgl_client_city is not None:
      j["doc"]["ipgl_client_city"] = i.ipgl_client_city
    if i.ipgl_client_postal_code is not None:
      j["doc"]["ipgl_client_postal_code"] = i.ipgl_client_postal_code
    if i.ipgl_client_longitude is not None:
      j["doc"]["ipgl_client_longitude"] = i.ipgl_client_longitude
    if i.ipgl_client_latitude is not None:
      j["doc"]["ipgl_client_latitude"] = i.ipgl_client_latitude
    if i.ipgl_client_isp_name is not None:
      j["doc"]["ipgl_client_isp_name"] = i.ipgl_client_isp_name
    if i.ipgl_client_organization_name is not None:
      j["doc"]["ipgl_client_organization_name"] = i.ipgl_client_organization_name
    if i.ipgl_client_autonomous_system_number is not None:
      j["doc"]["ipgl_client_autonomous_system_number"] = i.ipgl_client_autonomous_system_number
    if i.ipgl_client_autonomous_system_name is not None:
      j["doc"]["ipgl_client_autonomous_system_name"] = i.ipgl_client_autonomous_system_name
    if i.ipgl_server_country is not None:
      j["doc"]["ipgl_server_country"] = i.ipgl_server_country
    if i.ipgl_server_region is not None:
      j["doc"]["ipgl_server_region"] = i.ipgl_server_region
    if i.ipgl_server_city is not None:
      j["doc"]["ipgl_server_city"] = i.ipgl_server_city
    if i.ipgl_server_postal_code is not None:
      j["doc"]["ipgl_server_postal_code"] = i.ipgl_server_postal_code
    if i.ipgl_server_longitude is not None:
      j["doc"]["ipgl_server_longitude"] = i.ipgl_server_longitude
    if i.ipgl_server_latitude is not None:
      j["doc"]["ipgl_server_latitude"] = i.ipgl_server_latitude
    if i.ipgl_server_isp_name is not None:
      j["doc"]["ipgl_server_isp_name"] = i.ipgl_server_isp_name
    if i.ipgl_server_organization_name is not None:
      j["doc"]["ipgl_server_organization_name"] = i.ipgl_server_organization_name
    if i.ipgl_server_autonomous_system_number is not None:
      j["doc"]["ipgl_server_autonomous_system_number"] = i.ipgl_server_autonomous_system_number
    if i.ipgl_server_autonomous_system_name is not None:
      j["doc"]["ipgl_server_autonomous_system_name"] = i.ipgl_server_autonomous_system_name

    insert_list.append(j)
    batch_cmd = {"batch" : {"docs": insert_list}}
   # print batch_cmd
    if flash>batch_size:
      resp = requests.post(url='http://10.164.6.171:1123/TTLP/shard2',headers={'Content-Type': 'application/json'},json=batch_cmd)
      resp = requests.post(url='http://10.164.6.171:1123/TTLP/_shards/shard2',headers={'Content-Type': 'application/json'})
      print "{0}:Iteration: {1}, Num of records per Iteration {2}, Msg {3}".format(time.strftime("%H:%M:%S"),index, batch_size, resp.raise_for_status())
      flash=0


