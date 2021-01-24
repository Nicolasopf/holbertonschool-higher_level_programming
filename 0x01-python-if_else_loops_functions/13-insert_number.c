#include "lists.h"

/**
 * insert_node - Inserts a new node.
 * @head: Head.
 * @number: Num to insert into single linked list.
 * Return: NULL if fails, otherwise return the pointer to node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}

	tmp = *head;

	if (tmp->n > number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp->next)
	{
		if (tmp->n <= number && tmp->next->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
