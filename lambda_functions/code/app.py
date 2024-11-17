import requests, os

def lambda_handler(event, context):
	print(event)
	print("hello....")
	print(os.environ['secret'])