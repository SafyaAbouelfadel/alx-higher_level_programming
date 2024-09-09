#include "listes.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check if linked list is a cycle
 *
 * @list: linked list to check
 *
 * Return: 1 if is a cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
