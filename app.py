from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pretty Pri 💖</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(to right, #ff9a9e, #fad0c4);
    text-align: center;
    height: 100vh;
    margin: 0;
    overflow: hidden;
}
h1 {
    margin-top: 18vh;
    color: white;
    font-size: 2rem;
    padding: 0 16px;
}

button {
    padding: 16px 28px;
    font-size: 1.2rem;
    border: none;
    border-radius: 14px;
    margin: 12px;
    cursor: pointer;
}
#yes { background: #4CAF50; color: white; }
#no {
    background: #f44336;
    color: white;
    position: absolute;
}
@media (max-width: 480px) {
    h1 {
        font-size: 1.6rem;
    }
    button {
        width: 70%;
        max-width: 260px;
    }
}
</style>
</head>

<body>

<h1>Will you be my Valentine, Pretty Pri? 💘</h1>

<button id="yes" onclick="window.location.href='/yes'">Yes 💖</button>
<button id="no">No 💔</button>

<script>
const noBtn = document.getElementById("no");
function move() {
    noBtn.style.left = Math.random() * (window.innerWidth - 120) + "px";
    noBtn.style.top = Math.random() * (window.innerHeight - 120) + "px";
}
noBtn.addEventListener("mouseenter", move);
noBtn.addEventListener("touchstart", move);
</script>

</body>
</html>
"""

@app.route("/yes")
def yes():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YES 💖</title>
</head>
<body style="text-align:center; background:#ffe6f0;">
<h1>YAY! 💕</h1>
<img src="https://media.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif" width="300">
</body>
</html>
"""

if __name__ == "__main__":
    app.run(port=5050, debug=True)