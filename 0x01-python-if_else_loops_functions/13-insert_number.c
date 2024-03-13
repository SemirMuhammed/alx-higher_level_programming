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

    new = malloc(sizeof(listint_t));
    new->n = number;
    new->next = NULL;
    if (*head == NULL)
    {
        *head = new;
        return (new);
    }
    else if (number < (*head)->n)
    {
        new->next = *head;
        *head = new;
        return (new);
    }

    current = *head;

    do
    {
        if (current->next == NULL)
        {
            current->next = new;
            return (new);
        }
        temp = current;
        current = current->next;
    } while (number > current->n);
    temp->next = new;
    new->next = current;
    return (new);
}

