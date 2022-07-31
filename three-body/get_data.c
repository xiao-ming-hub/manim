#include <time.h>
#include <stdlib.h>
#include <stdio.h>
void show_2dv(const double (*x)[3], char n) {
  printf("        self.%c = np.array([", n);
  for (int i = 0; i < 3; i++) {
    putchar('[');
    for (int j = 0; j < 3; j++)
      printf("%lf%s", x[i][j], j ^ 2 ? ", " : (i ^ 2 ? "], " : "]"));
  }
  puts("])");
}
void show_ans(const double (*x)[3], const double (*v)[3], const double *m) {
  show_2dv(v, 'v');
  show_2dv(x, 'x');
  printf("        m = (");
  for (int i = 0; i < 3; i++)
    printf("%lf%s", m[i], i ^ 2 ? ", " : ")\n");
}
double drand() {
  int x = rand();
  double ans = x / (double)RAND_MAX - 0.5;
  ans *= 2;
  return ans;
}
int main() {
  srand(time(NULL));
  double x[3][3], v[3][3], m[3], ek = 0., e = 0., v2; // 动能和，引力势能和
  const double G = 9.8;
  for (int i = 0; i < 2; i++) x[i][2] = v[i][2] = 0.;
  while (1) {
    // 随机生成
    for (int i = 0; i < 3; i++) for (int j = 0; j < 2; j++)
      x[i][j] = drand(), v[i][j] = drand();
    for (int i = 0; i < 3; i++) m[i] = drand();
    for (int i = 0; i < 3; i++) {
      // 计算动能
      v2 = 0.;
      for (int j = 0; j < 3; j++) v2 += v[i][j] * v[i][j];
      ek += m[i] * v2;
    }
    ek *= 0.5;
    for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++)
      if (i ^ j) e += m[i] * m[j];
    e *= -G * 0.5;
    if (ek + e < 0.) break;
  }
  show_ans(x, v, m);
  return 0;
}
