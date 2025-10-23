{
  "caCert": "/etc/suite-connector/iothub.crt",
  "provisioningFile": "/etc/suite-connector/provisioning.json",
  "logFile": "/var/log/suite-connector/suite-connector.log",
  "address": "mqtts://hono.eclipseprojects.io:8883",
  "tenantId": "demo",
  "deviceId": "demo:device",
  "authId": "demo_device",
  "password": "secret_password"
}

{
  "caCert": "/etc/suite-connector/iothub.crt",
  "provisioningFile": "/etc/suite-connector/provisioning.json",
  "logFile": "/var/log/suite-connector/suite-connector.log",
  "address": "mqtts://hono.eclipseprojects.io:8883",
  "tenantId": "hnr",
  "deviceId": "hnr:orin",
  "authId": "hnr_orin",
  "password": "tuan_dz"
}

# The Hono tenant to be created
export TENANT=hnr
# The identifier of the device on the tenant
# Note! It's important for the ID to follow the convention namespace:name (e.g. demo:device)
export DEVICE_ID=hnr:orin
# The authentication identifier of the device
export AUTH_ID=hnr_orin
# A password for the device to authenticate with
export PWD=tuan_dz
