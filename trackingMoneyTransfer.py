import requests
import json
import pdb

def get_block_by_number(url: str, headers: dict, params: str) -> dict:
  payload = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": [params, False],"id":1}
  # HTTPレスポンスの形に変換
  r = requests.post(url, headers = headers, data = json.dumps(payload))
  return r.json()

def get_transaction_by_hash(url: str, headers: dict, params: str) -> dict:
  payload = {"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": [params],"id":1}
  # HTTPレスポンスの形に変換
  r = requests.post(url, headers = headers, data = json.dumps(payload))
  return r.json()

def main():
  url = 'https://rinkeby.infura.io/v3/17e3767c6f3f48acad8f96a5916ef08a'
  headers = {'content-type': 'application/json'}
  # 送金に関わったアカウント数の変数の作成
  num_of_account = 0
  # 送金に関わったアカウントリストの配列の作成
  account_list = []
  # それぞれの送金に関する総金額の配列の作成, from to eth
  transfer_money_list = []

  capital_transaction = get_transaction_by_hash(url, headers, "0x4c86c6b2c176f0720f02f92adcf4044817e1e2bd76a518a4c2fd0e2429c5d29b")
  num_of_account += 1
  account_list.append(capital_transaction['result']['to'])
  transfer_money_list.append([capital_transaction['result']['from'], capital_transaction['result']['to'], int(capital_transaction['result']['value'], 16)/1000000000000000000])

  #4103835から4103935までループ
  for num in range(int(capital_transaction['result']['blockNumber'], 16)+1, 4103936):
    block_buf = get_block_by_number(url, headers, str(hex(num)))
    transaction_hash_list = block_buf['result']['transactions']
    #pdb.set_trace()
    for transaction_hash in transaction_hash_list:
      transaction = get_transaction_by_hash(url, headers, transaction_hash)
      for account in account_list:
        if transaction['result']['from'] == account:
          #pdb.set_trace()
          num_of_account += 1
          account_list.append(transaction['result']['to'])
          transfer_money_list.append([transaction['result']['from'], transaction['result']['to'], int(transaction['result']['value'], 16)/1000000000000000000])

  # 実行結果
  print("Number of Account: " + str(num_of_account))
  print("Accounts: {")
  for account in account_list:
    print(account)
  print("}")
  print("Transactions:")
  for transfer_money in transfer_money_list:
    print("from: " + transfer_money[0] + ",   to: " + transfer_money[1] + ",   send: " + str(transfer_money[2]) + "ETH")

if __name__ == '__main__':
  main()
