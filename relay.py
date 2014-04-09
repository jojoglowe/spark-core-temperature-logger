import librato, json, requests, socket, time, os
from sseclient import SSEClient

librato_user = os.environ['LIBRATO_USER']
librato_auth = os.environ['LIBRATO_AUTH']

spark_core_id = os.environ['SPARK_CORE_ID']
spark_core_token = os.environ['SPARK_CORE_TOKEN']

librato_api = librato.connect(librato_user, librato_auth)
spark_messages = SSEClient("https://api.spark.io/v1/devices/%s/events/?access_token=%s" % (spark_core_id, spark_core_token))

while True:
  try:
    for msg in spark_messages:
      if msg.event == "temperature1":
        data = json.loads(msg.data);
        print "Decoded data:", data
        librato_api.submit("temperature", data['data'], description="temperature of fermenter 1", source="fermenter1")
  except socket.gaierror:
    print "Connection error. Trying again in a minute."
    time.sleep(60)
  except requests.exceptions.HTTPError:
    print "504 Server error. Trying again in a minute."
    time.sleep(60)
    spark_messages = SSEClient("https://api.spark.io/v1/devices/%s/events/?access_token=%s" % (spark_core_id, spark_core_token))