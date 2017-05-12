# !/bin/bash

#cd ./eth-utils

echo "Starting Node 0"
geth --datadir=./930925/data/00   --identity=00   --port=31100   --verbosity 3 --ipcdisable   --password=<(echo -n 00) --nodiscover  --rpc --rpcport=8200 --rpccorsdomain='*' --rpcapi='db,eth,net,web3,personal,web3' --networkid 930925 --mine  2>&1 | tee ./930925/log/00.log > ./930925/log/00.log.back &  # comment out if you pipe it to a tty etc.

