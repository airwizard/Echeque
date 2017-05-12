# !/bin/bash

echo "Initial cluster"
geth --datadir=./930925/data/00   --networkid 930925 --nodiscover  --rpc  --rpccorsdomain='*' init ./genesis.json     # comment out if you pipe it to a tty etc.

geth --datadir=./930925/data/01   --networkid 930925 --nodiscover  --rpc  --rpccorsdomain='*' init ./genesis.json     # comment out if you pipe it to a tty etc.

geth --datadir=./930925/data/02   --networkid 930925 --nodiscover  --rpc  --rpccorsdomain='*' init ./genesis.json     # comment out if you pipe it to a tty etc.

geth --datadir=./930925/data/03   --networkid 930925 --nodiscover  --rpc  --rpccorsdomain='*' init ./genesis.json     # comment out if you pipe it to a tty etc.

geth --datadir=./930925/data/04   --networkid 930925 --nodiscover  --rpc  --rpccorsdomain='*' init ./genesis.json     # comment out if you pipe it to a tty etc.


