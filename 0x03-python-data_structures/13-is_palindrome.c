#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int is_palindrome(listint_t **head)
{
	listint_t *counter = *head;
	listint_t *amiddle = *head;
	listint_t *bmiddle = *head;

	int count = 0;
	int idx = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (counter)
	{
		count++;
		counter = counter->next;
	}
	while (idx != count / 2)
	{
		bmiddle = bmiddle->next;
		idx++;
	}
	reverse_listint(&bmiddle);
	while (amiddle && bmiddle)
	{
		if (amiddle->n != bmiddle->n)
			return (0);
		amiddle = amiddle->next;
		bmiddle = bmiddle->next;
	}
	return (1);
}

/**
 * reverse_listint - Reverse a linked list
 * @head: List to be reversed
 * Return: The list reversed
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
