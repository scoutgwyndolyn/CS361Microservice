# CS361Microservice
COMMUNICATION CONTRACT:
1. to send data, "run.txt" will be updated to carry the command and the filepath of the desired excel spreadsheet. the microservice will execute and then exit as soon as it sees
"run
<filename>"

2. to receive data, wait for the microservice to exit and then read in the contents of "output.yaml". Sections of data will be separated by a line of "!!python/object/apply:collections.Counter", followed by key/value pairs containing the microservice's response
![image](https://github.com/scoutgwyndolyn/CS361Microservice/assets/71569880/3264eae2-82b5-4972-ac2e-63c6e0c32626)
