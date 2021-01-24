#include "lists.h"

/**
 * is_palindrome - Check if the Single linked list is palindrome
 * @head: Pointer to the head of the singled linked list.
 * Return: 1 if is a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int data[4096];
	int i = 0, j = 0;
	listint_t *tmp;

	if (!head)
		return (0);

	tmp = *head;

	if (!*head || (*head)->next == NULL)
		return (1);

	for (; tmp; tmp = tmp->next, i++)
		data[i] = tmp->n;
	for (; i > j; i--, j++)
	{
		if (data[i - 1] != data[j])
			return (0);
	}
	return (1);
}
