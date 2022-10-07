#include<stdio.h>
#include<stdlib.h>

struct Node* head;
struct Node
{
	int data;
	struct Node* next;
};

// inserts elements at starting of the list
void Insert(int i)
{
	Node* temp=(Node*)malloc(sizeof(struct Node));
	(*temp).data=i;
	(*temp).next=head;
	head=temp;
};

void InsertAtPosition(int i,int pos)
{
	struct Node* temp_head=head;
	Node* temp_node = (Node*)malloc(sizeof(struct Node));
	temp_node->data = i;
	if(pos==0)
	{
		temp_node->next=head;
		head=temp_node;
		return;
	}
	
	for(int j=0;j<pos;j++)
	{
		temp_head=temp_head->next;
	}
	
	temp_node->next=temp_head->next;
}


void Append(int i)
{
	struct Node* now = head;
	Node* temp=(Node*)malloc(sizeof(struct Node));
	while(now!=NULL)
	{
		now=now->next;
	}
	
	temp->data=i;
	temp->next=NULL;
	now->next=temp;
	
}

void Print()
{
	struct Node* temp = head;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
	printf("\n");
};

int main()
{
	head = NULL;
	printf("How many numbers for the list ?\n");
	int n,x,pos;
	scanf("%d",&n);
	
	for(int i=0;i<n;i++)
	{
//		printf("list the numbers ?\n");
//		scanf("%d",&x);
//		printf("please give the position \n");
//		scanf("%d",&pos);
//		Insert(x);
		InsertAtPosition(1,0);
		InsertAtPosition(2,1);
		InsertAtPosition(3,2);
		InsertAtPosition(4,3);
		InsertAtPosition(5,4);
		
//		Append(x);
		Print();
	}
}
