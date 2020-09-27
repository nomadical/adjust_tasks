<h1>Task 1</h1>

There're two solutions for the task:
The first one is python based and the second solution are just bunch of bash commands.

Just run the script_1.0.sh or script_2.0.sh :)


<br/>
<br/>
<h1>Task 2</h1>


<h3>1. Below are the metrics I consider as interesting to monitor</h3>

<h4>a) Metrics on CPU</h4>
<br/>
Temperature<br/>
Used part<br/>
Load<br/>

<h4>b) Metrics on memory</h4>
<br/>
Mem. usage<br/>
Mem. used<br/>
<br />
Disk space usage<br/>

<h4>c) Input and Output stats</h4>
<br/>
Read/Write stats
<br/>
<h4>d) Network</h4>
<br/>
Traffic info
<br/>
<h3>2. Custom bash script could be written for each metrics value for special cases, if necessary, but in a usual case I would monitor them with Zabbix and set relevant custom notification alerts for various overloads and limit reaches.</h3>

<br />
<br/>
<h2>Challenges of monitoring</h2>
<br/>
<h3>1. Deciding which metrics are really necessary and which is not important for the case.</h3>
<br/>
<h3>2. Proper choice and setting of the monitoring system, so it won't influence server's performance.</h3>
<br/>
<h3>3. Making sure alerts set are precise and couldn't cause false cautions.</h3>
