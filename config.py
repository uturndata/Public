config = {

    # AWS credentials for the IAM user (alternatively can be set up as environm$

    'aws_access_key': '',
    'aws_secret_key': '',

    # EC2 info about your server's region
    'ec2_region_name': 'us-east-1',
    'ec2_region_endpoint': 'ec2.us-east-1.amazonaws.com',

    # Tag of the EBS volume you want to take the snapshots of
    #'tag_name': 'tag:MakeSnapshot',
    'tag_name': 'MakeSnapshot',
    'tag_value': 'True',

    # Number of snapshots to keep (the older ones are going to be deleted,
    # since they cost money).
    'keep_day': DayNumber,
    'keep_week': WeekNumber,
    'keep_month': MonthNumber,

    # Path to the log for this script
    'log_file': '/tmp/makesnapshots.log',

    # ARN of the SNS topic (optional)
    'arn': 'ReplaceWithSNSARN',

    # Proxy config (optional)
    #'proxyHost': '10.100.x.y',
    #'proxyPort': '8080'
}

