//Aluno: Augusto Cesar B dos Santos 
//Metodos da bissecao e secante

#include<stdio.h>
#include<math.h>

int passos;

//fiz uma pra cada caso kkkkk
double bissecao(double a, double b, double epsilon);
double bissecao2(double a, double b, double epsilon);
double bissecao3(double a, double b, double epsilon);
double secante(double a, double b, double epsilon);
double secante2(double a, double b, double epsilon);
double secante3(double a, double b, double epsilon);

double funcaoA(double x){
    return pow(x, 5) - (2 * pow(x, 4)) + (22 * pow(x, 3)) + (4 * pow(x, 1)) - 24;
}

double funcaoB(double x){
    return cos(x) - sqrt(x);
}
double funcaoC(double x){
    return ((sqrt(x) - 5) * exp(-x));
}

int main(void){
    
    passos = 0;
    double resultado = bissecao (1, 3, 1e-10);
    printf("Bissecao == %.20lf ===== %d passos\n", resultado, passos);
    double resultado2 = bissecao2 (0, 1, 1e-10);
    printf("Bissecao == %.20lf ===== %d passos\n", resultado2, passos);
    double resultado3 = bissecao3 (23, 26, 1e-10);
    printf("Bissecao == %.20lf ===== %d passos\n", resultado3, passos);

    double resultado4 = secante (1, 3, 1e-10);
    printf("Secante == %.20lf ===== %d passos\n", resultado4, passos);
    double resultado5 = secante2 (0, 1, 1e-10);
    printf("Secante == %.20lf ===== %d passos\n", resultado5, passos);
    double resultado6 = secante3 (23, 26, 1e-10);
    printf("Secante == %.20lf ===== %d passos\n", resultado6, passos);

    return 0;
}

double bissecao(double a, double b, double epsilon){
    double x0 = a, x1 = b;

    do{
        x0 = x1;
        x1 = (a + b)/2;

        if(funcaoA(x1) * funcaoA(a) < 0){
            b = x1;
            passos++;
        }
        else{
            a = x1;
            passos++;
        }

    } while(fabs(x1 - x0) > epsilon);

    return x0;
}
double bissecao2(double a, double b, double epsilon){
    double x0 = a, x1 = b;

    do{
        x0 = x1;
        x1 = (a + b)/2;

        if(funcaoB(x1) * funcaoB(a) < 0){
            b = x1;
            passos++;
        }
        else{
            a = x1;
            passos++;
        }

    } while(fabs(x1 - x0) > epsilon);

    return x0;
}
double bissecao3(double a, double b, double epsilon){
    double x0 = a, x1 = b;

    do{
        x0 = x1;
        x1 = (a + b)/2;

        if(funcaoC(x1) * funcaoC(a) < 0){
            b = x1;
            passos++;
        }
        else{
            a = x1;
            passos++;
        }

    } while(fabs(x1 - x0) > epsilon);

    return x0;
}

double secante(double a, double b, double epsilon){
    double x0 = a, x1 = b, x2;
    while (fabs(x1 - x0) > epsilon) {
        x2 = x1 - funcaoA(x1) * (x1 - x0) / (funcaoA(x1) - funcaoA(x0));
        x0 = x1;
        x1 = x2;
    }
  return x1;
}
double secante2(double a, double b, double epsilon){
    double x0 = a, x1 = b, x2;
    while (fabs(x1 - x0) > epsilon) {
        x2 = x1 - funcaoB(x1) * (x1 - x0) / (funcaoB(x1) - funcaoB(x0));
        x0 = x1;
        x1 = x2;
    }
  return x1;
}
double secante3(double a, double b, double epsilon){
    double x0 = a, x1 = b, x2;
    while (fabs(x1 - x0) > epsilon) {
        x2 = x1 - funcaoC(x1) * (x1 - x0) / (funcaoC(x1) - funcaoC(x0));
        x0 = x1;
        x1 = x2;
    }
  return x1;
}