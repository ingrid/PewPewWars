require.config({
	baseUrl:"js/jam/jam/"
});
require(['jam'], function(jam){
var ws;
    // Variables.
    var conn, game;

    // Functions.
    var openConnection;

    if (window.MozWebSocket) {
        // Firefox is special.
        window.WebSocket = window.MozWebSocket;
    }

    // Move websocket code to a jam module?
    ws = new WebSocket("ws://localhost:8888/ws/echo");
    ws.onopen = function() {
        ws.send("Don't panic.");
    };
    ws.onmessage = function(event) {
        alert("The server sent a message: " + event.data);
    };

    game = jam.Game(500, 300, document.body);
    player = jam.Sprite(10, 100);
    setInterval(
        function(){
            console.log(ws.readyState);
        }, 100);
});