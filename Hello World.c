#include <stdio.h>
#include <stdlib.h>

typedef char *(*fp_t)(void);
typedef int (*printer_t)(const char *, ...);

char h(void) { return 72; }
char e(void) { return 101; }
char l(void) { return 108; }
char o(void) { return 111; }
char space(void) { return 32; }
char w(void) { return 119; }
char r(void) { return 114; }
char d(void) { return 100; }
char n(void) { return 10; }

char *get_message(void) {
    static char msg[13]; /* "Hello world\n" + terminating NUL = 13 */
    msg[0]  = h();
    msg[1]  = e();
    msg[2]  = l();
    msg[3]  = l();
    msg[4]  = o();
    msg[5]  = space();
    msg[6]  = w();
    msg[7]  = o();
    msg[8]  = r();
    msg[9]  = l();
    msg[10] = d();
    msg[11] = n();
    msg[12] = '\0';
    return msg;
}

int exec(void) {
    fp_t f = get_message;
    printer_t p = printf;
    /* call printf with the generated string as the format */
    return p(f());
}

/* return a pointer to exec (keeps the indirection you used earlier) */
int (*entry(void))(void) {
    return exec;
}

/* proper C entry point */
int main(void) {
    return entry()();
}
