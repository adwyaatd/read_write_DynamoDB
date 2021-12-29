import boto3
from boto3.dynamodb.conditions import Key,Attr


def main():
  dynamoDB = boto3.resource("dynamodb")
  table = dynamoDB.Table("ESM")
  query_data = table.query(
    IndexName='GSI1',
    KeyConditionExpression = Key("SK").eq("shop") & Key("PK").begins_with("shop_")
  )
  print(query_data)
  shops = query_data["Items"]
  # print(shops)
  return shops


def lambda_handler(event, context):
  try:
    shops = main()
    response = {
      "statuscode": 200,
      "data": shops
    }
    return response
  except Exception as e:
    print("Error")
