#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to check if a singly linked list has a cycle. */
int check_cycle(listint_t *list) {
    if (list == NULL || list->next == NULL) {
        return 0; // No cycle if list is empty or has only one node
    }

    listint_t *slow = list; // Slow pointer moves one step at a time
    listint_t *fast = list->next; // Fast pointer moves two steps at a time

    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return 1; // Cycle detected
        }
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0; // No cycle found
}

/* Utility function to create a new node */
listint_t *create_node(int data) {
    listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    new_node->n = data;
    new_node->next = NULL;
    return new_node;
}

/* Utility function to free the memory allocated for the list */
void free_list(listint_t *list) {
    listint_t *temp;
    while (list != NULL) {
        temp = list;
        list = list->next;
        free(temp);
    }
}

int main() {
    // Create a sample linked list with a cycle
    listint_t *head = create_node(1);
    head->next = create_node(2);
    head->next->next = create_node(3);
    head->next->next->next = head->next; // Creating a cycle

    // Check if the linked list has a cycle
    int has_cycle = check_cycle(head);
    printf("Does the linked list have a cycle? %s\n", has_cycle ? "Yes" : "No");

    // Free the memory allocated for the list
    free_list(head);

    return 0;
}