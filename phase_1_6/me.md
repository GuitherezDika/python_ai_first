source venv/bin/activate
uvicorn app.main:app --reload

or
uvicorn app.main:app --reload --host 0.0.0.0

cek ip di terminal 
ifconfig | grep "inet " | grep -v 127
= 192.168.73.94 netmask 0xfffffe00 broadcast 192.168.73.255
= hasil nya = 192.168.73.94 

static const String _url = 'ws://192.168.73.94:8000/ws/chat';

reload backend
reload flutter
====