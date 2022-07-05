#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *temp = *head;
	int head_val, tail_val;

	/* empty list condition */
	if (*head == NULL || (*head)->n == NULL)
		return(1);

	/* get head value*/
	head_val = (*head)->n;
	while (current)
	{
		/* look ahead to see if next node from current is tail */
		if ((current->next)->next == NULL)
		{
			tail_val = (current->next)->n;
			/* update tail */
			current->next = NULL;
			if (head_val != tail_val)
				return 0; /* not palindrome */

			temp = temp->next;
			if(!temp)
				break;

			head_val = temp->n;
			current = temp;
		}
		else
			current = current->next;
	}
	return 1; /* is palindrome */
}
