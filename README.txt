A simple messageboard in Django using Node.js and socket.io to update messages in realtime.

To get it setup make sure to run $: npm install
in a Django environment run $: python manage.py runserver
as well as $: node server.js

to get live updating to work be sure to change src="http://192.168.1.17:8001/socket.io/socket.io.js" to whatever your local IP address is
this is found in both the templates folder in wall.html and in the partials folder in wall_partial.html


