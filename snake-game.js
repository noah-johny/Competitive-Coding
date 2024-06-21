const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const objectSize = 24;
const canvasSize = 400;
const gameSpeed = 150;

let timeoutId = null;

function gameLoop() {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(function onTick() {
    clearCanvas();
    drawFood();
    moveAndUpdateSnake();
    drawSnake();
    checkGameOver();
    if (!isGameOver) {
      requestAnimationFrame(gameLoop);
    }
  }, gameSpeed);
}

function drawSnakePart(snakePart) {
  ctx.fillStyle = "lightgreen";
  ctx.beginPath();
  ctx.arc(
    snakePart.x + objectSize / 2,
    snakePart.y + objectSize / 2,
    objectSize / 2,
    0,
    2 * Math.PI
  );
  ctx.fill();
  ctx.stroke();
}

function drawSnake() {
  snake.forEach(drawSnakePart);
}

function drawFood() {
  ctx.fillStyle = "red";
  ctx.beginPath();
  ctx.arc(
    food.x + objectSize / 2,
    food.y + objectSize / 2,
    objectSize / 2,
    0,
    2 * Math.PI
  );
  ctx.fill();
}

function clearCanvas() {
  ctx.fillStyle = "#0a0a0a";
  ctx.fillRect(0, 0, canvasSize, canvasSize);
}

function moveAndUpdateSnake() {
  let headX = snake[0].x + dx;
  let headY = snake[0].y + dy;

  if (headX >= canvasSize) {
    headX = 0;
  } else if (headX < 0) {
    headX = canvasSize - objectSize;
  }
  if (headY >= canvasSize) {
    headY = 0;
  } else if (headY < 0) {
    headY = canvasSize - objectSize;
  }

  const newHead = { x: headX, y: headY };

  const hasEatenFood = headX === food.x && headY === food.y;
  if (hasEatenFood) {
    score += 10;
    createFood();
  } else {
    snake.pop();
  }

  snake.unshift(newHead);
}

function randomFood(min, max) {
  return (
    Math.round((Math.random() * (max - min) + min) / objectSize) * objectSize
  );
}

function createFood() {
  food.x = randomFood(0, canvasSize - objectSize);
  food.y = randomFood(0, canvasSize - objectSize);
  snake.forEach(function isFoodOnSnake(part) {
    const foodIsOnSnake = part.x == food.x && part.y == food.y;
    if (foodIsOnSnake) createFood();
  });
}

function checkGameOver() {
  for (let i = 1; i < snake.length; i++) {
    if (snake[0].x === snake[i].x && snake[0].y === snake[i].y) {
      isGameOver = true;

      if ("fonts" in document) {
        document.fonts.load('10pt "Inter"').then(function () {
          displayGameOver();
        });
      }
      break;
    }
  }
}

function displayGameOver() {
  clearCanvas();
  ctx.globalAlpha = 0.5;

  drawSnake();
  drawFood();

  ctx.globalAlpha = 1.0;
  ctx.font = "48px Inter";
  ctx.fillStyle = "red";
  ctx.textAlign = "center";
  ctx.fillText("Game Over", canvas.width / 2, canvas.height / 2);
}

function changeDirection(event) {
  const LEFT_KEY = 37;
  const RIGHT_KEY = 39;
  const UP_KEY = 38;
  const DOWN_KEY = 40;

  const keyPressed = event.keyCode;
  const goingUp = dy === -objectSize;
  const goingDown = dy === objectSize;
  const goingRight = dx === objectSize;
  const goingLeft = dx === -objectSize;

  if (keyPressed === LEFT_KEY && !goingRight) {
    dx = -objectSize;
    dy = 0;
  }
  if (keyPressed === UP_KEY && !goingDown) {
    dx = 0;
    dy = -objectSize;
  }
  if (keyPressed === RIGHT_KEY && !goingLeft) {
    dx = objectSize;
    dy = 0;
  }
  if (keyPressed === DOWN_KEY && !goingUp) {
    dx = 0;
    dy = objectSize;
  }
}

document.addEventListener("keydown", changeDirection);

function startGame() {
  isGameOver = false;
  gameLoop();
}

function resetGame() {
  snake = [{ x: objectSize * 5, y: objectSize * 5 }];
  food = { x: objectSize * 10, y: objectSize * 10 };
  dx = objectSize;
  dy = 0;
  score = 0;
  isGameOver = true;

  clearCanvas();
  drawFood();
  drawSnake();
}

resetGame();

document.getElementById("startBtn").addEventListener("click", startGame);
document.getElementById("resetBtn").addEventListener("click", resetGame);
