function drawSquare() {
    const title = document.getElementsByClassName("title")[0];
    const titleSize = title.clientWidth;

    const canvas = document.getElementsByClassName("canvas")[0];
    const ctx = canvas.getContext("2d");

    const beginX = (canvas.width - titleSize * 1.1)/2;
    const endX = (canvas.width + titleSize * 1.1)/2;

    ctx.beginPath();
    ctx.moveTo(beginX, 0);
    ctx.lineTo(0, 0);
    ctx.lineTo(0, 283);
    ctx.lineTo(1097, 283);
    ctx.lineTo(1097, 0);
    ctx.lineTo(endX, 0);
    ctx.strokeStyle = "white";
    ctx.lineWidth = 3;
    ctx.stroke();
}

screen.onload = drawSquare()