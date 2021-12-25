import boto3
from boto3.dynamodb.conditions import Key,Attr

def put_item(table):
  table.put_item(
    Item = {
      "PartitionKey": "shop_1",
      "SortKey": "shop_1"
    }
  )

def main():
  dynamoDB = boto3.resource("dynamodb")
  print("type(dynamoDB)")
  print(type(dynamoDB))
  print("dynamoDB")
  print(dynamoDB)
  print("-----------------")
  table = dynamoDB.Table("ESM")
  print("type(table)")
  print(type(table))
  print("table")
  print(table)
  print("-----------------")

  query_data = table.query(
    KeyConditionExpression = Key("PK").eq("shop_1")
  )
  print("type(query_data)")
  print(type(query_data))
  print("query_data")
  print(query_data)
  print("-----------------")

  shops = query_data["Items"]
  print("type(shops)")
  print(type(shops))
  print("shops")
  print(shops)
  print("-----------------")
  for shop in shops:
    print("type(shop)")
    print(type(shop))
    print(shop)
    print(shop["PK"])
    print("-----------------")

def lambda_handler(event, context):
  try:
    main()
  except Exception as e:
    print("Error")
