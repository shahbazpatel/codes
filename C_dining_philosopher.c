#include<stdio.h>
#include<semaphore.h>
#include<pthread.h>
//gcc  C_dining_philosopher.c -lpthread -o dp
#define N 5
#define HUNGRY 1
#define THINKING 0
#define EATING 2
#define LEFT (phil_id + 4) % N
#define RIGHT	(phil_id + 1)




sem_t mutex;
sem_t S[N];

int state[N];
int phil_arr[N] = {0, 1, 2, 3, 4};

void *philospher(void *num);
void take_fork(int);
void put_fork(int);
void test(int);


void *philosopher(void *num){
		while(1){
				int *i = num;
				sleep(1);
				take_fork(*i);
				sleep(1);
				put_fork(*i);
			
			}
	}

void take_fork(int phil_id){
		sem_wait(&mutex);
		state[phil_id] = HUNGRY;
		printf("\n Philospher %d is hungry", phil_id+1);
		test(phil_id);
		sem_post(&mutex);
		sem_wait(&S[phil_id]);
		sleep(1);
	
	}


void test(int phil_id){
		if(state[phil_id] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING){
				state[phil_id] = EATING;
				sleep(2);
				printf("\nPhilosopher %d takes fork %d and %d", phil_id+1, LEFT+1, phil_id+1);
				printf("\nPhilospher %d is eating", phil_id+1);
				sem_post(&S[phil_id]);
			
			}
	
	
	}

void put_fork(int phil_id){
		sem_wait(&mutex);
		state[phil_id] = THINKING;
		printf("\nPhilosopher %d is putting fork %d and %d down", phil_id+1, LEFT+1, phil_id+1);
		printf("\nPhilosopher %d is thinking", phil_id+1);
		test(LEFT);
		test(RIGHT);
		sem_post(&mutex);
	}


main(){
	int i;
	pthread_t thread_id[N];  	//creating 5 threads
	sem_init(&mutex, 0, 1);		//initializing the semaphore

	for(i = 0; i < N; i++){
		sem_init(&S[i], 0, 0);
	}

	for(i = 0; i < N; i++){
			pthread_create(&thread_id[i], NULL, philosopher, &phil_arr[i]);
			printf("\nPhilosopher %d is thinking", i+1);		
		}
	for(i = 0; i < N; i++){
			pthread_join(thread_id[i], NULL);
		}
	
	}


