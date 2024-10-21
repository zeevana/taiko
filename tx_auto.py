import random
import time
from web3 import Web3

# Excluded wallet address (replace with the wallet you want to exclude)
excluded_wallet = '0xde2DbBD06b55b6c9A1893d99c8760dDb912411a0'

# Function to get user input with secure private key entry
def get_input():
    provider_url = input('Enter the JSON RPC Provider URL: ')
    private_key = input('Enter your private key: ')
    num_receivers = int(input('Enter the number of receiver wallets: '))
    
    receiver_wallets = []
    for i in range(num_receivers):
        receiver_wallet = input(f'Enter receiver wallet address {i + 1}: ')
        if receiver_wallet.lower() == excluded_wallet.lower():
            print(f'This wallet ({receiver_wallet}) is excluded from transfers. Skipping...')
        else:
            receiver_wallets.append(receiver_wallet)
    
    amount_to_send = input('Enter the amount to transfer (in ETH): ')
    interval_min = int(input('Enter the minimum interval time (in milliseconds): '))
    interval_max = int(input('Enter the maximum interval time (in milliseconds): '))

    return provider_url, private_key, receiver_wallets, amount_to_send, interval_min, interval_max

# Function to connect to Ethereum network and send transactions
def send_transactions(provider_url, private_key, receiver_wallets, amount_to_send, interval_min, interval_max):
    try:
        # Connect to the Ethereum node
        web3 = Web3(Web3.HTTPProvider(provider_url))
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum network.")

        # Convert ETH to Wei
        amount_in_wei = web3.toWei(amount_to_send, 'ether')
        
        # Get account details
        account = web3.eth.account.privateKeyToAccount(private_key)
        print(f"Connected to account: {account.address}")
        
        # Get gas price (randomized within a range)
        min_gas_price = web3.toWei('1', 'gwei')
        max_gas_price = web3.toWei('2', 'gwei')

        while True:
            # Random interval for bot behavior obfuscation
            random_interval = random.randint(interval_min, interval_max) / 1000  # Convert to seconds

            # Random gas price and gas limit
            gas_price = random.randint(min_gas_price, max_gas_price)
            min_gas_limit = 90000
            max_gas_limit = 110000
            gas_limit = random.randint(min_gas_limit, max_gas_limit)

            # Get nonce and balance
            nonce = web3.eth.getTransactionCount(account.address, 'pending')
            balance = web3.eth.getBalance(account.address)
            tx_buffer = web3.toWei(0.0005, 'ether')

            if balance - tx_buffer >= amount_in_wei:
                print("New balance detected... Sending transactions...")

                # Iterate through receiver wallets
                for receiver in receiver_wallets:
                    try:
                        tx = {
                            'nonce': nonce,
                            'to': receiver,
                            'value': amount_in_wei,
                            'gas': gas_limit,
                            'gasPrice': gas_price
                        }
                        signed_tx = web3.eth.account.signTransaction(tx, private_key)
                        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                        print(f"Transaction hash: {web3.toHex(tx_hash)}")
                        print(f"Total amount sent: {amount_to_send} ETH to {receiver}")
                        nonce += 1
                    except Exception as e:
                        print(f"Error sending to {receiver}: {e}")
                    finally:
                        # Add random delay between transactions
                        delay = random.uniform(1, 3)  # Random delay between 1 to 3 seconds
                        print(f"Waiting for {delay} seconds before next transaction...")
                        time.sleep(delay)
            else:
                print(f"Insufficient balance to send {amount_to_send} ETH")

            # Random delay before repeating the process
            print(f"Waiting for {random_interval} seconds before the next batch of transactions...")
            time.sleep(random_interval)

    except Exception as e:
        print(f"Error occurred: {e}")

# Main program
if __name__ == "__main__":
    provider_url, private_key, receiver_wallets, amount_to_send, interval_min, interval_max = get_input()
    send_transactions(provider_url, private_key, receiver_wallets, amount_to_send, interval_min, interval_max)
