[comment]: # "Auto-generated SOAR connector documentation"
# ForeScout CounterACT

Publisher: Splunk  
Connector Version: 2.0.6  
Product Vendor: ForeScout  
Product Name: CounterACT  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.1.1  

This app implements various network access control actions for ForeScout

[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2018-2024 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""


This app requires  **CounterACT 8.0** or above with the **eyeExtend Connect Module** installed. When
the eyeExtend Connect Module is installed, Web API and Data Exchange (DEX) modules will be
available. Web API is a read-only module, while DEX is a read and write module.





In the case of restricting updates to CounterACT, only supply Web API credentials in the asset
configuration.



## Playbook Backward Compatibility

-   The existing action parameters have been modified in the actions given below. Hence, it is
    requested to the end-user to please update their existing playbooks by re-inserting | modifying
    | deleting the corresponding action blocks or by providing appropriate values to these action
    parameters to ensure the correct functioning of the playbooks created on the earlier versions of
    the app.

      

    -   get device info - Added two new parameters for this action.

          

        -   The parameters 'host_ip' and 'host_mac' have been added.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a CounterACT asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**device** |  required  | string | IP Address of appliance (ie: 10.10.10.10)
**ph_0** |  optional  | ph | Placeholder
**dex_account** |  optional  | string | Data Exchange (DEX) account name
**dex_username** |  optional  | string | Data Exchange (DEX) username
**dex_password** |  optional  | password | Data Exchange (DEX) password
**ph_1** |  optional  | ph | Placeholder
**web_username** |  optional  | string | Web API username
**web_password** |  optional  | password | Web API password
**verify_server_cert** |  optional  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[list hosts](#action-list-hosts) - List hosts in CounterACT  
[list policies](#action-list-policies) - List policies in CounterACT  
[get device info](#action-get-device-info) - Get the properties of a host  
[get sessions](#action-get-sessions) - Get active sessions in CounterACT  
[install firewall](#action-install-firewall) - Install a virtual firewall with a property  
[delete property](#action-delete-property) - Delete a property of a host  
[update property](#action-update-property) - Update a property of a host  
[update list](#action-update-list) - Update a list by adding, deleting, or deleting all values from it  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'list hosts'
List hosts in CounterACT

Type: **investigate**  
Read only: **True**

This action requires Web API credential in asset configuration.

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data.\*.ip | string |  `ip`  |   10.1.16.161 
action_result.data.\*.mac | string |  `forescout mac address`  `mac address`  |  
action_result.data.\*.hostId | numeric |  `forescout host id`  |   167841953 
action_result.data.\*.links.\*.href | string |  `url`  |   https://10.1.16.161/api/hosts/167841953 
action_result.data.\*.links.\*.rel | string |  |   self 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Num hosts: 2 
action_result.summary.num_hosts | numeric |  |   2 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list policies'
List policies in CounterACT

Type: **investigate**  
Read only: **True**

This action requires Web API credential in asset configuration.

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data.\*.rules.\*.ruleId | numeric |  `forescout rule id`  |   1822401057983693948 
action_result.data.\*.rules.\*.description | string |  |   When a device is NAT, its other classifications may be inaccurate. Therefore, we put the NAT detection first. 
action_result.data.\*.rules.\*.name | string |  |   NAT Devices 
action_result.data.\*.policyId | numeric |  `forescout policy id`  |   -6488799636120036097 
action_result.data.\*.description | string |  |   Classify the hosts into the following groups for easier management:

1. NAT devices
2. Windows systems
3. Linux/Unix systems
4. Macintosh systems
5. Network gear
6. Printers
7. Unclassified

Required parameters:
Network Segment

Method:
Re-classification is done on every admission and at least once a day using passive and active fingerprinting. 
action_result.data.\*.name | string |  |   Asset Classification 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Num policies: 1 
action_result.summary.num_policies | numeric |  |   1 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get device info'
Get the properties of a host

Type: **investigate**  
Read only: **True**

One of the parameters (host_id, host_ip, or host_mac) is required and the first to be provided is used (in that order). This action requires Web API credential in asset configuration.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host_id** |  optional  | Host ID of device (Used first, if provided) | numeric |  `forescout host id` 
**host_ip** |  optional  | Current local IP address of device (Used second, if provided) | string |  `ip` 
**host_mac** |  optional  | Host MAC address of device (Used last, if provided) | string |  `forescout mac address`  `mac address` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.host_id | numeric |  `forescout host id`  |   167841953 
action_result.parameter.host_ip | string |  `ip`  |   203.0.113.1 
action_result.parameter.host_mac | string |  `forescout mac address`  `mac address`  |   00:50:56:8b:00 
action_result.data.\*.ip | string |  `ip`  |   10.1.16.161 
action_result.data.\*.mac | string |  `forescout mac address`  `mac address`  |   00:50:56:8b:00 
action_result.data.\*.id | numeric |  `forescout host id`  |   167841953 
action_result.data.\*.fields.onsite.timestamp | numeric |  |   1537079515 
action_result.data.\*.fields.onsite.value | string |  |   true 
action_result.data.\*.fields.comment.timestamp | numeric |  |   1537296024 
action_result.data.\*.fields.comment.value | string |  |   Test Comment 
action_result.data.\*.fields.access_ip.timestamp | numeric |  |   1537296024 
action_result.data.\*.fields.access_ip.value | string |  `ip`  |   10.1.16.161 
action_result.data.\*.fields.samba_open_ports.timestamp | numeric |  |   1537296024 
action_result.data.\*.fields.samba_open_ports.value | string |  |   0 
action_result.data.\*.fields.user_def_fp.timestamp | numeric |  |   1537297213 
action_result.data.\*.fields.user_def_fp.value | string |  |   CounterACT Appliance 
action_result.data.\*.fields.fsapi_Prop_String.timestamp | numeric |  |   1537306598 
action_result.data.\*.fields.fsapi_Prop_String.value | string |  |   mystring 
action_result.data.\*.fields.va_netfunc.timestamp | numeric |  |   1537297213 
action_result.data.\*.fields.va_netfunc.value | string |  |   CounterACT Device 
action_result.data.\*.fields._times.\*.timestamp | numeric |  |   1537315647 
action_result.data.\*.fields._times.\*.value | string |  |   last_onsite 
action_result.data.\*.fields.online.timestamp | numeric |  |   1537315647 
action_result.data.\*.fields.online.value | string |  |   true 
action_result.data.\*.fields.misc.timestamp | numeric |  |   1537297255 
action_result.data.\*.fields.misc.value | string |  |   3\* \* openports 1937755350365319853 1 1537297229 0 0 openports -7973166747367276753 1 1537297229 0 0 openports -3101146461677770228 1 1537297229 0 0 \*  
action_result.data.\*.fields.last_nbt_report_time.timestamp | numeric |  |   1537296028 
action_result.data.\*.fields.last_nbt_report_time.value | string |  |   1537296028 
action_result.data.\*.fields.cl_type.timestamp | numeric |  |   1537297213 
action_result.data.\*.fields.cl_type.value | string |  |   Managed(CounterACT) 
action_result.data.\*.fields.fingerprint.timestamp | numeric |  |   1537297213 
action_result.data.\*.fields.fingerprint.value | string |  |   CounterACT Device 
action_result.data.\*.fields.fsapi_Prop_Test.timestamp | numeric |  |   1537306902 
action_result.data.\*.fields.fsapi_Prop_Test.value | string |  |   test 
action_result.data.\*.fields.ctdevtype.timestamp | numeric |  |   1537315647 
action_result.data.\*.fields.ctdevtype.value | string |  |   appliance 
action_result.data.\*.fields.cl_rule.timestamp | numeric |  |   1537297213 
action_result.data.\*.fields.cl_rule.value | string |  |   counteract 
action_result.data.\*.fields.engine_seen_packet.timestamp | numeric |  |   1537315647 
action_result.data.\*.fields.engine_seen_packet.value | string |  |   true 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Host id: 10.1.16.161 
action_result.summary.host_ip | string |  `ip`  |   10.1.16.161 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get sessions'
Get active sessions in CounterACT

Type: **investigate**  
Read only: **True**

This action requires Web API credential in asset configuration.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**rule_id** |  optional  | Comma separated list of policies or policy sub-rules | string |  `forescout rule id`  `forescout policy id` 
**prop_val** |  optional  | Comma separated list of host property values (ie: Prop_String=Sales,Prop_Int=5) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.prop_val | string |  |   fsapi_Prop_String=mystring, fsapi_Prop_Test=test 
action_result.parameter.rule_id | string |  `forescout rule id`  `forescout policy id`  |   7042988451856611698 
action_result.data.\*.ip | string |  `ip`  |   10.1.16.1  10.1.16.161 
action_result.data.\*.mac | string |  `forescout mac address`  `mac address`  |   00:50:56:8b:00 
action_result.data.\*.hostId | numeric |  `forescout host id`  |   167841793  167841953 
action_result.data.\*.links.\*.href | string |  `url`  |   https://10.1.16.161/api/hosts/167841793  https://10.1.16.161/api/hosts/167841953 
action_result.data.\*.links.\*.rel | string |  |   self 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Num active sessions: 5 
action_result.summary.num_active_sessions | numeric |  |   5 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'install firewall'
Install a virtual firewall with a property

Type: **generic**  
Read only: **False**

This action requires DEX credential in asset configuration.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host_key_name** |  required  | Type of identifier used to specify the endpoint | string | 
**host_key_value** |  required  | IP or MAC address of the virtual firewall to install | string |  `forescout mac address`  `mac address`  `ip` 
**property_name** |  required  | The property that will be added | string |  `forescout property name` 
**property_value** |  required  | The value of the property | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.property_value | string |  |   new vfw 
action_result.parameter.property_name | string |  `forescout property name`  |   Prop_String 
action_result.parameter.host_key_value | string |  `forescout mac address`  `mac address`  `ip`  |   10.1.16.3 
action_result.parameter.host_key_name | string |  |   ip 
action_result.data.\*.response_code | string |  |   FSAPI_OK 
action_result.data.\*.response_message | string |  |   Successfully updated [1] properties for new host [ip=10.1.16.3] 
action_result.data.\*.host_key_value | string |  `forescout mac address`  `mac address`  `ip`  |   10.1.16.3 
action_result.data.\*.host_key_name | string |  |   ip 
action_result.data.\*.property_value | string |  |   new vfw 
action_result.data.\*.property_name | string |  `forescout property name`  |   Prop_String 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Message: Successfully updated [1] properties for new host [ip=10.1.16.3] 
action_result.summary.message | string |  |   Successfully updated [1] properties for new host [ip=10.1.16.3] 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'delete property'
Delete a property of a host

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host_key_name** |  required  | Type of identifier used to specify the host | string | 
**host_key_value** |  required  | Identifier value used to specify the host | string |  `forescout mac address`  `mac address`  `ip` 
**property_name** |  required  | The property that will be deleted | string |  `forescout property name` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.property_name | string |  `forescout property name`  |   Prop_Test 
action_result.parameter.host_key_value | string |  `forescout mac address`  `mac address`  `ip`  |   10.1.16.161 
action_result.parameter.host_key_name | string |  |   ip 
action_result.data.\*.property_name | string |  `forescout property name`  |   Prop_Test 
action_result.data.\*.response_code | string |  |   FSAPI_OK 
action_result.data.\*.host_key_name | string |  |   ip 
action_result.data.\*.host_key_value | string |  `ip`  |   10.1.16.161 
action_result.data.\*.response_message | string |  |   Successfully deleted 1 properties for [ip=10.1.16.161] 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Message: Successfully deleted 1 properties for [ip=10.1.16.161] 
action_result.summary.message | string |  |   Successfully deleted 1 properties for [ip=10.1.16.161] 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'update property'
Update a property of a host

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration.<p>The created new host will be only seen on UI when the host value is in the range of IP segment configured in ForeScout CounterACT.</p><p>The property_name field is the Property Tag field of Property created in CounterACT. This action won’t support composite type of property.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host_key_name** |  required  | Type of identifier used to specify the host | string | 
**host_key_value** |  required  | Identifier value used to specify the host | string |  `forescout mac address`  `mac address`  `ip` 
**property_name** |  required  | The property that will be modified | string |  `forescout property name` 
**property_value** |  required  | The new value of the property | string | 
**create_host** |  optional  | If set to true and the host is not known to CounterACT, create a new host | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.create_host | boolean |  |   True  False 
action_result.parameter.host_key_value | string |  `forescout mac address`  `mac address`  `ip`  |   10.1.16.161 
action_result.parameter.host_key_name | string |  |   ip 
action_result.parameter.property_value | string |  |   property_value 
action_result.parameter.property_name | string |  `forescout property name`  |   Prop_String 
action_result.data.\*.response_code | string |  |   FSAPI_OK 
action_result.data.\*.response_message | string |  |   Successfully updated [1] properties for host [ip=10.1.16.161] 
action_result.data.\*.host_key_value | string |  `ip`  |   10.1.16.161 
action_result.data.\*.host_key_name | string |  |   ip 
action_result.data.\*.property_value | string |  |   property_value 
action_result.data.\*.property_name | string |  `forescout property name`  |   Prop_String 
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Message: Successfully updated [1] properties for host [ip=10.1.16.161] 
action_result.summary.message | string |  |   Successfully updated [1] properties for host [ip=10.1.16.161] 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'update list'
Update a list by adding, deleting, or deleting all values from it

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**action** |  required  | Type of update for list | string | 
**list_name** |  required  | Name of list to update | string | 
**values** |  optional  | Comma separated list of values to update. This field is required for add_list_values and delete_list_values actions | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.action | string |  |   add_list_values  delete_all_list_values 
action_result.parameter.list_name | string |  |   Prop_List 
action_result.parameter.values | string |  |   hello  hello, goodbye  v1, v2, v3, v4, v5 
action_result.data | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |   Message: Successfully added values to the [1] lists. 
action_result.summary.message | string |  |   Successfully added values to the [1] lists. 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 