function solution(a, b) {
  a = a.toString();
  b = b.toString();
  const ab = a + b;
  const ba = b + a;

  if (ab > ba) {
    return Number(ab);
  } else if (ab < ba) {
    return Number(ba);
  } else {
    return Number(ab);
  }
}
