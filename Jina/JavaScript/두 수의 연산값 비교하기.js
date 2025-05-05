function solution(a, b) {
  const ab_num = 2 * a * b;

  a = a.toString();
  b = b.toString();
  const ab = a + b;

  if (ab >= ab_num) {
    return Number(ab);
  } else {
    return ab_num;
  }
}
