const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = +input[0];
// [상담에 걸리는 일수, 받을 수 있는 돈]
const ls = input.slice(1).map((line) => line.split(" ").map(Number));
const dp = Array(N + 1).fill(0);

for (let i = N - 1; i >= 0; i--) {
  const [time, pay] = ls[i];
  if (i + time > N) {
    dp[i] = dp[i + 1];
  } else {
    dp[i] = Math.max(dp[i + 1], pay + dp[i + time]);
  }
}

console.log(dp[0]);
