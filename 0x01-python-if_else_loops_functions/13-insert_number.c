#include "lists.h"

/**
 * insert_node - inserts a new node at the tail of a linked list
 * @head : pointer to the head of the linked list
 * @number : integer to be included in the new node
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;
	listint_t *copy;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (temp && temp->n < number)
	{
		copy = temp;
		temp = temp->next;
	}
	copy->next = new;
	new->next = temp;
	return (new);
}
