#include "lists.h"

/**
 * check_cycle - Check if a single linked list have a cycle.
 * @list: single linked list
 * Return: 1 if have a cycle, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *f1 = NULL, *f2 = NULL;

	f1 = list, f2 = list;
	while (list && f1 && f2 && f1->next && f2->next)
	{
		f1 = f1->next;
		f2 = f2->next->next;
		if (!f2 || !f1)
			return (0);
		if (f2->next == f1)
			return (1);
	}
	return (0);
}
