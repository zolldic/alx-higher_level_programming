#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: (0) if there is no cycle or (1) if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);

	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
