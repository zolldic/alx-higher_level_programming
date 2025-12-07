#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: (0) if there is no cycle or (1) if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	
	head = list;

	while (head->next != NULL)
	{
		head = head->next;
		if (head == list)
			return (1);
	}

	return (0);
}
