Uturn QuickStart	
Start - Stop - SnapShot	

Utility server that uses tags to autostart, autostop and snapshot volumes. 

Overview
Amazon currently lacks automation around some key functions include:
•	The ability to start in stop instances on a schedule.
•	The ability to automatically snapshot EBS volumes and store them for standard retention times.
This Quickstart uses a Cloud Formation template to create a single t2.micro instance that requires minimal management it in turn uses tags to target EC2 instances and EBS volumes to control: starting, stopping and snapshotting. The Cloud Formation template also creates a Cloudwatch alarm and an email SNS topic as well an IAM Role that allows the Instance to access the AWS API endpoint. The instance will need access to the public API endpoint to operate.

Design
An instance is deployed with a Role that allows it to act upon instances in volumes within the region.  While the two scripts operate in a similar manner they have been written buy different developers and are implemented separately.

You can find the original source repositories here:
https://schen1628.wordpress.com/2014/02/04/auto-start-and-stop-your-ec2-instances/
and
https://github.com/evannuil/aws-snapshot-tool

Parameters
Key			Example 						Note					
AmiID			ami-146e2a7c				Use the AWS Linux 
DefaultSG		sg-f6ff2892					If you need to SSH
EmailSNSAlarm	your@Domain.com				Where do you want notifications sent
InstanceType	t2.micro					Mirco should be fine	
KeyName			uturn-prod					SSH key
UtilSubnet		subnet-c8bb38bf				VPC Subnet to run.
DayNumber		7							Number of Day snapshots to retain .
WeekNumber		4							Number of Weekly snapshots to retain.
MonthNumber		12							Number of Monthly snapshots to retain.
APIEndpoint		ec2.us-east-1.amazonaws.com	Valid API End point
Region 			us-east-1					Valid region for AWS

Tags
Name				Example 		note			
auto:start  		0 14 * * * 		valid cron entry
auto:stop 			0 14 * * *		valid cron entry
MakeSnapshot		True			Only True is needed


Start and Stop
The EC2 instance looks for the auto:start and auto:stop tags to determine when to start and stop instances. The name of the tags are case-sensitive. The value of the tags should be in a cron format. For instance, 0 14 * * * is 2 pm everyday. The time is based on the OS time of the EC2 operator instance. If you have not changed the default time zone of the EC2 operator instance, it should be in UTC. It will ignore any instances that do not have the tags set or the format is invalid. The auto:start tag holds the start schedule, and the auto:stop tag holds the stop schedule. Do not tag the EC2 operator instance, otherwise it will get stopped by itself.

SnapShot EBS 
Simply add a tag “MakeSnapshot” and set value to “True” to each volume you want to snapshot, It will handle rolling snapshots on a day, week and year so that you can setup the retention policy to suit. The Config.py file sets the retention schedule and can be modified easily.

'keep_day': 7,
'keep_week': 5,
'keep_month': 13,


Resource Summary and List
Logical ID					Type                  	
StopStartSnapServerSNS		AWS::SNS::Topic	
OperatorRole				AWS::IAM::Role	
OperatorInstanceProfile		AWS::IAM::InstanceProfile	
OperatorInstance			AWS::EC2::Instance
ServerDown					AWS::CloudWatch::Alarm

Code 
https://github.com/uturndata/Public
