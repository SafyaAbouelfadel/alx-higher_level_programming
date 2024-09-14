#include "lists.h"

/**
 * palindrom -  recursive palind or not
 * @head: head list to check
 * Return: 0 if not a palindrome
 * 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindrome(head, *head));
}

/**
 * aux_palindrome - helper function to check if the list is a palindrome
 * @head: double pointer to the head of the list (updated during recursion)
 * @end: pointer to the current node at the end of the list
 * Return: 1 if the list is a palindrome, 0 if not
 */

int aux_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
