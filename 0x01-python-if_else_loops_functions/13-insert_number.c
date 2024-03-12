#include "lists.h"
#include <stdio.h>

/**
 * insert_node - insert number into sorted linked list
 * @head: head of sorted linked list
 * @number: number to insert
 *
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp, *current, *new;

    if (*head == NULL)
        return (NULL);

    current = *head;
    new = malloc(sizeof(listint_t));
    new->n = number;
    new->next = NULL;

    while (current)
    {
        if (current->n >= number)
        {
            temp->next = new;
            new->next = current;
            break;
        }
        temp = current;
        current = current->next;
    }
    return (new);
}

