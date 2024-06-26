#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    pid_t pid = fork();
    if (pid == 0)
    {
        // child process
        printf("printf from child %d.\n", getpid());
    }
    else
    {
        // parent process
        printf("mine PID is %d - child PID is %d\n", getpid(), pid);
    }
}
