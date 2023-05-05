//retrieve node in DOM via ID
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");
ctx.fillStyle = "rgb(0, 255, 255)";
var requestID;

var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height); //just wipes everything inside the slate
}

var radius = 250;
var growing = true;

var drawDot = () => {
    console.log("test");
    console.log(radius);
    window.cancelAnimationFrame(requestID);
    /*
        Wipe the canvas,
        Repaint the circle,

        ...and somewhere (where/when is the right time?)
        Update request ID to propagate the animation.
        You will need
        window.cancelAnimationFrame()
        window.requestAnimationFrame()
    */
    clear();
    //ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ")";

    if (radius >= 250) {
        growing = false;
    }

    if (radius <= 0) {
        growing = true;
    }

    if (growing) {
        radius++;
    } else {
        radius--;
    }

    ctx.beginPath();
    ctx.arc(250, 250, radius,0,Math.PI*2);
    //ctx.arc(Math.floor(Math.random()*250), Math.floor(Math.random()*250), radius,0,Math.PI*2);
    ctx.fill();
    requestID = window.requestAnimationFrame(drawDot);
    console.log("request ID:" + requestID);
};

//var stopIt = function() {
var stopIt = ()=> {
    console.log("stopIt invoked...");
    console.log( requestID );

    window.cancelAnimationFrame(requestID);

    /* YOUR CODE HERE
        ... to stop the animation
        You will need window.cancelAnimationFrame()
    */
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);