# !/bin/bash

#cd ./eth-utils

echo "Starting Node 0"
geth --datadir=./930925/data/00   --identity=00   --port=31100   --verbosity 3 --ipcdisable   --nodiscover  --rpc --rpcport=8200 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925 --mine  2>&1 | tee ./930925/log/00.log > ./930925/log/00.log.back &  # comment out if you pipe it to a tty etc.

echo "Starting Node 1"
geth --datadir=./930925/data/01   --identity=01   --port=31101   --verbosity 3 --ipcdisable   --nodiscover  --rpc --rpcport=8201 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925  2>&1 | tee ./930925/log/01.log > ./930925/log/01.log.back &  # comment out if you pipe it to a tty etc.

echo "Starting Node 2"
geth --datadir=./930925/data/02   --identity=02   --port=31102   --verbosity 3 --ipcdisable   --nodiscover  --rpc --rpcport=8202 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925   2>&1 | tee ./930925/log/02.log > ./930925/log/02.log.back &  # comment out if you pipe it to a tty etc.

echo "Starting Node 3"
geth --datadir=./930925/data/03   --identity=03   --port=31103   --verbosity 3 --ipcdisable   --nodiscover  --rpc --rpcport=8203 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925   2>&1 | tee ./930925/log/03.log > ./930925/log/03.log.back  &  # comment out if you pipe it to a tty etc.

echo "Starting Node 4"
geth --datadir=./930925/data/04   --identity=04   --port=31104   --verbosity 3 --ipcdisable   --nodiscover  --rpc --rpcport=8204 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925   2>&1 | tee ./930925/log/04.log > ./930925/log/04.log.back &  # comment out if you pipe it to a tty etc.

