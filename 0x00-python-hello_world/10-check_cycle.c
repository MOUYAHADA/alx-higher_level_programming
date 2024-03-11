#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: list head
 * Return: 1 if there is a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *last = list, *first = list;

	if (!list)
		return (0);

	while (last && first && fast->next)
	{
		last = last->next;
		fast = first->next->next;

		if (last == first)
			return (1);
	}

	return (0);
}