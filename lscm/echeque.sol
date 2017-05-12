pragma solidity 0.4.10;

contract EchequeSystem {
    string bankName;
    string monetaryUnit;
    address bankAddress;
    mapping (address => uint) balances;
    address[] _tempa;
    uint[] _tempi;

    
    struct EchequeStruct {
        string drawer;
        string payee;
        bool negotiable;
        bool issue_flag;
        uint amount;
        address[] owner;
    }
    
    mapping (uint => EchequeStruct) EchequeNoList;
    mapping (address => uint[]) ownEchequeList;


    function EchequeSystem(address _bankAddress, string _bankName, string _monetaryUnit) {
        bankAddress = _bankAddress;
        bankName = _bankName;
        monetaryUnit = _monetaryUnit;
    }

    function deposit(address _account, uint _amount) {
        if (msg.sender != bankAddress) throw;
        balances[_account] += _amount;
    }
    
    function issueEcheque(string _drawer, string _payee, uint _amount, uint _EchequeNo) {
        if (balances[msg.sender] < _amount) throw;
        if (_amount == 0) throw;
        balances[msg.sender] -= _amount;
        _tempa = [msg.sender];
        if (sha3(_payee) == sha3('None')) {
            EchequeNoList[_EchequeNo] = EchequeStruct({drawer: _drawer, payee:_payee, negotiable: true, issue_flag:true, amount:_amount, owner:_tempa});
        }
        else {
            EchequeNoList[_EchequeNo] = EchequeStruct({drawer: _drawer, payee:_payee, negotiable: false, issue_flag:true, amount:_amount, owner:_tempa});
        }
        uint[] a = ownEchequeList[msg.sender];
        a.push(_EchequeNo);
        ownEchequeList[msg.sender] = a;
    }
    
    
    function transferEcheque(address _to, uint _EchequeNo) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        if (e.amount == 0) throw;
        if (e.owner[e.owner.length - 1] != msg.sender) throw;
        if (e.issue_flag == false) throw;
        e.owner.push(_to);
        EchequeNoList[_EchequeNo] = e;
        
        uint[] a = ownEchequeList[msg.sender];
        uint _len = a.length;
        uint j = 0;
        _tempi.length = _len-1;
        for (uint i=0; i<_len; i++){
            if (a[i] != _EchequeNo) {
                _tempi[j] = a[i];
                j++;
            }
        }
        ownEchequeList[msg.sender] = _tempi;
        
        uint[] b = ownEchequeList[_to];
        b.push(_EchequeNo);
        ownEchequeList[_to] = b;
        
    }
    
    function cashEcheque(string _payee, uint _EchequeNo) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        if (e.amount == 0) throw;
        if (e.owner[e.owner.length - 1] != msg.sender) throw;
        if (e.issue_flag == false) throw;
        if (e.negotiable == false && sha3(e.payee) != sha3(_payee)) throw;
        
        balances[msg.sender] += e.amount;
        e.issue_flag == false;
        EchequeNoList[_EchequeNo] = e;
        
        uint[] a = ownEchequeList[msg.sender];
        uint _len = a.length;
        uint j = 0;
        _tempi.length = _len-1;
        for (uint i=0; i<_len; i++){
            if (a[i] != _EchequeNo) {
                _tempi[j] = a[i];
                j++;
            }
        }
        ownEchequeList[msg.sender] = _tempi;
    }

    function getBalance(address _account) constant returns (uint) {
        return balances[_account];
    }
    
    function getBankName() constant returns (string) {
        return bankName;
    }
    
    function getMonetaryUnit() constant returns (string) {
        return monetaryUnit;
    }
    
    function traceEchequeOwner(uint _EchequeNo) constant returns (address[]) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        return e.owner;
    }
    
    function getEchequeAmount(uint _EchequeNo) constant returns (uint) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        return e.amount;
    }
    
    function getEchequeDrawer(uint _EchequeNo) constant returns (string) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        return e.drawer;
    }
    
    function getEchequePayee(uint _EchequeNo) constant returns (string) {
        EchequeStruct e = EchequeNoList[_EchequeNo];
        return e.payee;
    }
    
    function ifEchequeValid(uint _EchequeNo) constant returns (bool){
        EchequeStruct e = EchequeNoList[_EchequeNo];
        if (e.amount == 0) return false;
        return e.issue_flag;
    }
    
    function getEchequesByAccount(address _account) constant returns (uint[]) {
        return ownEchequeList[_account];
    }
    function getMsgSender() constant returns (address) {
        return msg.sender;
    }
}

