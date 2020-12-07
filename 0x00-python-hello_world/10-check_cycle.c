#include "lists.h"

/**
 * check_cycle - Check if a single linked list have a cycle.
 * @list: single linked list
 * Return: 1 if have a cycle, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *s1, *s2;

	if (!list)
		return (0);
	s1 = list, s2 = list;

	while (s1 && s2 && s2->next)
	{
		s1 = s1->next, s2 = s2->next->next;
		if (s1 == s2)
			return (1);
	}
	return (0);
}
