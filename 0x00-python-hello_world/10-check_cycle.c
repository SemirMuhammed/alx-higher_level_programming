#include "lists.h"

/**
 * check_cycle - efficiently check if the linked list has loop
 * @list: the linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = slow = list;

	while (fast)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

