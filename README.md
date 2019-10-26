###### Snapshot

###### Version 1.0

###### Description

Simple python app which monitor the system and output information in the plain text file and  json file (configurable in config.json).

#### Gathered information

The application will gather the follow information:  
  - CPU usage (percent);  
  - physical disk used and total Mbytes;  
  - virtual memory used and total Mbytes;  
  - input/ouput disk operations;  
  - network sent/received Mbytes.  

The information will be written to txt or jsont file(need to specify in config.json)


#### Installation

Wheel-package is in `devops_lab` directory.  
To install use

`pip install pip install devops_lab/`


#### Usage

`$ python devops_lab`

To run application type `python devops_lab`.  


#### Output Examples

####Json

![Image](/images/txt.png)

####Json

![Image](/images/json.png)