#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - loop
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombie process
 * Return: 0 at success
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == -1)
		{
			perror("Error creating zombie process");
			exit(EXIT_FAILURE);
		}
		else if (zombie_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (0);
}
