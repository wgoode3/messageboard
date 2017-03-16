# Messageboard

A simple messageboard in Django using Node.js and socket.io to update messages in realtime.

## Install

To get it setup make sure to run 

```
$ npm install
```

In a Django environment run 

```
$ python manage.py runserver
```

To get live updating to work be sure to change

```
<script type ="text/javascript" src="http://192.168.1.17:8001/socket.io/socket.io.js"></script>
var socket = io.connect('http://192.168.1.17:8001');
```

To whatever your local IP address is. This is found in both the templates folder in wall.html and in the partials folder in wall_partial.html.

In a second console window run
```
$ node server.js
```


  



