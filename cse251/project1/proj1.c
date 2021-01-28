#include <stdio.h>
#include <math.h>


#define MAX_N 100000
#define MIN_N 10
#define ERROR 1e-10


double delta(int a, int b, int n)
{
    return (b - a) / (double) n;
}

double sinc(double x)
{
    if (x == 0) {
        return 1;
    }

    return sin(M_PI * x) / (M_PI * x);
}

double equation(int a, int b, int n)
{
    double d, x, res;
    int i;

    d = delta(a, b, n);
    res = 0;

    for (i = 1; i <= n; i++) {
        x = a + (i - 0.5) * d;
        res += sinc(x);
    }

    return res * d;
}

int main(int argc, char **argv)
{
    double res, pre_res, decrease;
    int a, b, n;

    printf("Enter a value for a: ");
    scanf("%d", &a);
    printf("Enter a value for b: ");
    scanf("%d", &b);
    printf("Integral evaluation\n");

    pre_res = 0;
    for (n = MIN_N; n <= MAX_N; n++) {
        res = equation(a, b, n);
        decrease = res - pre_res;

        if (n == MIN_N) {
            printf("%d: %.9lf\n", n, res);
        } else {
            printf("%d: %.9lf %.9e\n", n, res, decrease);
        }

        if (decrease < ERROR && decrease > -ERROR) {
            printf("The integral result is %.9lf\n", res);
            return 0;
        }

        pre_res = res;

    }

    return 0;
}
