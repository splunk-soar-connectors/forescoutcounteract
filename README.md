[comment]: # "Auto-generated SOAR connector documentation"
# ForeScout CounterACT

Publisher: Splunk  
Connector Version: 2\.0\.3  
Product Vendor: ForeScout  
Product Name: CounterACT  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app implements various network access control actions for ForeScout

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2018-2022 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
<div>

This app requires  **CounterACT 8.0** or above with the **eyeExtend Connect Module** installed. When
the eyeExtend Connect Module is installed, Web API and Data Exchange (DEX) modules will be
available. Web API is a read-only module, while DEX is a read and write module.

</div>

<div>

In the case of restricting updates to CounterACT, only supply Web API credentials in the asset
configuration.

</div>

## Playbook Backward Compatibility

-   The existing action parameters have been modified in the actions given below. Hence, it is
    requested to the end-user to please update their existing playbooks by re-inserting \| modifying
    \| deleting the corresponding action blocks or by providing appropriate values to these action
    parameters to ensure the correct functioning of the playbooks created on the earlier versions of
    the app.

      

    -   get device info - Added two new parameters for this action.

          

        -   The parameters 'host_ip' and 'host_mac' have been added.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a CounterACT asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**device** |  required  | string | Hostname or IP of appliance \(ie\: 10\.10\.10\.10\)
**ph\_0** |  optional  | ph | Placeholder
**dex\_account** |  optional  | string | Data Exchange \(DEX\) account name
**dex\_username** |  optional  | string | Data Exchange \(DEX\) username
**dex\_password** |  optional  | password | Data Exchange \(DEX\) password
**ph\_1** |  optional  | ph | Placeholder
**web\_username** |  optional  | string | Web API username
**web\_password** |  optional  | password | Web API password
**verify\_server\_cert** |  optional  | boolean | Verify server certificate

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

This action requires Web API credential in asset configuration\.

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.ip | string |  `ip` 
action\_result\.data\.\*\.mac | string |  `forescout mac address`  `mac address` 
action\_result\.data\.\*\.hostId | numeric |  `forescout host id` 
action\_result\.data\.\*\.links\.\*\.href | string |  `url` 
action\_result\.data\.\*\.links\.\*\.rel | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.num\_hosts | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list policies'
List policies in CounterACT

Type: **investigate**  
Read only: **True**

This action requires Web API credential in asset configuration\.

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.rules\.\*\.ruleId | numeric |  `forescout rule id` 
action\_result\.data\.\*\.rules\.\*\.description | string | 
action\_result\.data\.\*\.rules\.\*\.name | string | 
action\_result\.data\.\*\.policyId | numeric |  `forescout policy id` 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.num\_policies | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get device info'
Get the properties of a host

Type: **investigate**  
Read only: **True**

One of the parameters \(host\_id, host\_ip, or host\_mac\) is required and the first to be provided is used \(in that order\)\. This action requires Web API credential in asset configuration\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host\_id** |  optional  | Host ID of device \(Used first, if provided\) | numeric |  `forescout host id` 
**host\_ip** |  optional  | Current local IP address of device \(Used second, if provided\) | string |  `ip` 
**host\_mac** |  optional  | Host MAC address of device \(Used last, if provided\) | string |  `forescout mac address`  `mac address` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.host\_id | numeric |  `forescout host id` 
action\_result\.parameter\.host\_ip | string |  `ip` 
action\_result\.parameter\.host\_mac | string |  `forescout mac address`  `mac address` 
action\_result\.data\.\*\.ip | string |  `ip` 
action\_result\.data\.\*\.mac | string |  `forescout mac address`  `mac address` 
action\_result\.data\.\*\.id | numeric |  `forescout host id` 
action\_result\.data\.\*\.fields\.onsite\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.onsite\.value | string | 
action\_result\.data\.\*\.fields\.comment\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.comment\.value | string | 
action\_result\.data\.\*\.fields\.access\_ip\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.access\_ip\.value | string |  `ip` 
action\_result\.data\.\*\.fields\.samba\_open\_ports\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.samba\_open\_ports\.value | string | 
action\_result\.data\.\*\.fields\.user\_def\_fp\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.user\_def\_fp\.value | string | 
action\_result\.data\.\*\.fields\.fsapi\_Prop\_String\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.fsapi\_Prop\_String\.value | string | 
action\_result\.data\.\*\.fields\.va\_netfunc\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.va\_netfunc\.value | string | 
action\_result\.data\.\*\.fields\.\_times\.\*\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.\_times\.\*\.value | string | 
action\_result\.data\.\*\.fields\.online\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.online\.value | string | 
action\_result\.data\.\*\.fields\.misc\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.misc\.value | string | 
action\_result\.data\.\*\.fields\.last\_nbt\_report\_time\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.last\_nbt\_report\_time\.value | string | 
action\_result\.data\.\*\.fields\.cl\_type\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.cl\_type\.value | string | 
action\_result\.data\.\*\.fields\.fingerprint\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.fingerprint\.value | string | 
action\_result\.data\.\*\.fields\.fsapi\_Prop\_Test\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.fsapi\_Prop\_Test\.value | string | 
action\_result\.data\.\*\.fields\.ctdevtype\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.ctdevtype\.value | string | 
action\_result\.data\.\*\.fields\.cl\_rule\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.cl\_rule\.value | string | 
action\_result\.data\.\*\.fields\.engine\_seen\_packet\.timestamp | numeric | 
action\_result\.data\.\*\.fields\.engine\_seen\_packet\.value | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.host\_ip | string |  `ip` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get sessions'
Get active sessions in CounterACT

Type: **investigate**  
Read only: **True**

This action requires Web API credential in asset configuration\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**rule\_id** |  optional  | Comma separated list of policies or policy sub\-rules | string |  `forescout rule id`  `forescout policy id` 
**prop\_val** |  optional  | Comma separated list of host property values \(ie\: Prop\_String=Sales,Prop\_Int=5\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.prop\_val | string | 
action\_result\.parameter\.rule\_id | string |  `forescout rule id`  `forescout policy id` 
action\_result\.data\.\*\.ip | string |  `ip` 
action\_result\.data\.\*\.mac | string |  `forescout mac address`  `mac address` 
action\_result\.data\.\*\.hostId | numeric |  `forescout host id` 
action\_result\.data\.\*\.links\.\*\.href | string |  `url` 
action\_result\.data\.\*\.links\.\*\.rel | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.num\_active\_sessions | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'install firewall'
Install a virtual firewall with a property

Type: **generic**  
Read only: **False**

This action requires DEX credential in asset configuration\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host\_key\_name** |  required  | Type of identifier used to specify the endpoint | string | 
**host\_key\_value** |  required  | IP or MAC address of the virtual firewall to install | string |  `forescout mac address`  `mac address`  `ip` 
**property\_name** |  required  | The property that will be added | string |  `forescout property name` 
**property\_value** |  required  | The value of the property | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.property\_value | string | 
action\_result\.parameter\.property\_name | string |  `forescout property name` 
action\_result\.parameter\.host\_key\_value | string |  `forescout mac address`  `mac address`  `ip` 
action\_result\.parameter\.host\_key\_name | string | 
action\_result\.data\.\*\.response\_code | string | 
action\_result\.data\.\*\.response\_message | string | 
action\_result\.data\.\*\.host\_key\_value | string |  `forescout mac address`  `mac address`  `ip` 
action\_result\.data\.\*\.host\_key\_name | string | 
action\_result\.data\.\*\.property\_value | string | 
action\_result\.data\.\*\.property\_name | string |  `forescout property name` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'delete property'
Delete a property of a host

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host\_key\_name** |  required  | Type of identifier used to specify the host | string | 
**host\_key\_value** |  required  | Identifier value used to specify the host | string |  `forescout mac address`  `mac address`  `ip` 
**property\_name** |  required  | The property that will be deleted | string |  `forescout property name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.property\_name | string |  `forescout property name` 
action\_result\.parameter\.host\_key\_value | string |  `forescout mac address`  `mac address`  `ip` 
action\_result\.parameter\.host\_key\_name | string | 
action\_result\.data\.\*\.property\_name | string |  `forescout property name` 
action\_result\.data\.\*\.response\_code | string | 
action\_result\.data\.\*\.host\_key\_name | string | 
action\_result\.data\.\*\.host\_key\_value | string |  `ip` 
action\_result\.data\.\*\.response\_message | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update property'
Update a property of a host

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration\.<p>The created new host will be only seen on UI when the host value is in the range of IP segment configured in ForeScout CounterACT\.</p><p>The property\_name field is the Property Tag field of Property created in CounterACT\. This action won’t support composite type of property\.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host\_key\_name** |  required  | Type of identifier used to specify the host | string | 
**host\_key\_value** |  required  | Identifier value used to specify the host | string |  `forescout mac address`  `mac address`  `ip` 
**property\_name** |  required  | The property that will be modified | string |  `forescout property name` 
**property\_value** |  required  | The new value of the property | string | 
**create\_host** |  optional  | If set to true and the host is not known to CounterACT, create a new host | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.create\_host | boolean | 
action\_result\.parameter\.host\_key\_value | string |  `forescout mac address`  `mac address`  `ip` 
action\_result\.parameter\.host\_key\_name | string | 
action\_result\.parameter\.property\_value | string | 
action\_result\.parameter\.property\_name | string |  `forescout property name` 
action\_result\.data\.\*\.response\_code | string | 
action\_result\.data\.\*\.response\_message | string | 
action\_result\.data\.\*\.host\_key\_value | string |  `ip` 
action\_result\.data\.\*\.host\_key\_name | string | 
action\_result\.data\.\*\.property\_value | string | 
action\_result\.data\.\*\.property\_name | string |  `forescout property name` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update list'
Update a list by adding, deleting, or deleting all values from it

Type: **correct**  
Read only: **False**

This action requires DEX credential in asset configuration\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**action** |  required  | Type of update for list | string | 
**list\_name** |  required  | Name of list to update | string | 
**values** |  optional  | Comma separated list of values to update\. This field is required for add\_list\_values and delete\_list\_values actions | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.action | string | 
action\_result\.parameter\.list\_name | string | 
action\_result\.parameter\.values | string | 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 