#include "lists.h"
#include <string.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: number to add to the linked list
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p, *n;
	
	if (!head)
		return (NULL);

	new = (listint_t *) malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	n = *head;

	while (n->n < number)
	{
		p = n;
		n = n->next;
	}

	new->next = n;
	p->next = new;
	
	return (new);
}
