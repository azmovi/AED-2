#include <stdio.h>
#include <pthreads.h>
#include <semaphores.h>
#include <unistd.h>
#include "fila.c"


#define N 10

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
sem_t barbeiro, cliente, barbeiro_pront, cliente_pronto;

Fila fila;

void lotado()
{
    printf("A Barbearia está lotada!\n");
    return;
}

void cliente_cortando()
{
    printf("Meu momento de cortar o cabelo\n");
    sleep(1);
    return;
}

void barbeiro_cortando()
{
    printf("Barbeiro está cortando o cabelo");
    sleep(1);
    return;
}

void *barbeiro(void *arg)
{
    while(1)
    {
        sem_wait(&cliente);
        pthread_threa_lock(&mutex);

        int cliente = remove(&fila);
        
        pthread_threa_unlock(&mutex);

    }
}

void *cliente(void *arg)
{
    return;
}
