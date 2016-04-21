//bfinal.cpp

#include<iostream>
#include<string>
using namespace std;
class binser
{	
public:	
	template<class T>
	int partition( T a[],int low,int high )	//partitioning the array
	{
		T num=a[low];	//pivot element (choosing 1st element of array as pivot element)
		int i=low+1;
		int j=high;
		T temp;
		while(1)
		{
		 	while(i<high && num>a[i])
		       		i++;
		       	while(num<a[j])
		       		j--;
		       	if( i<j )
		       	{
			  	temp=a[i];
			  	a[i]=a[j];
			  	a[j]=temp;
		      	 }
		       	else
		       	{
			  	temp=a[low];
			  	a[low]=a[j];
			  	a[j]=temp;
			  	return(j);
		       	}
		}
	}
	template<class T>
	void Quick(T a[],int low,int high )	//recursive quicksort
	{
		int j;
		if( low<high )
		{
		    j=partition(a,low,high);
		    Quick(a,low,j-1);	//recursive call for numbers between low and partition element
		    Quick(a,j+1,high );	//recursive call for numbers between partition and high element
		}
	}
	template <class T>
	void Bsearch(T *a, T item, int n)
	{
		int beg=0,end=n-1;
		int mid=(beg+end)/2;
		while(beg<=end && a[mid]!=item)      // Compare Item and Value of Mid
		{
			if(a[mid]<item)
				beg=mid+1;
			else
				end=mid-1;
			mid=(beg+end)/2;
		}
		if(a[mid]==item)
			cout<<"\nData is Found at Location : "<<mid+1<<endl;
		else
			cout<<"Data is Not Found!"<<endl;
	}
};
int main()
{
	int N,i,ch;	
	binser b;	
	do
	{
		cout<<"Press 1 for numbers else 2 for strings:";
		cin>>ch;
	}while(ch<1||ch>2);	
	cout<<"Enter array size : ";
	cin>>N;
	switch(ch)
	{
		case 1:
			{
				float *p=new float[N];
				float fele;				
				cout<<"\nEnter "<<N<<" no's..\n";
				for(i=0; i<N; i++ )
					cin>>p[i];
				cout<<"\nArray before sorting is..\n";
				for(i=0; i<N; i++ )
					cout<<p[i]<<"\n";
				b.Quick( p,0,N-1 );
				cout<<"\nArray after sorting is..\n";
				for(i=0; i<N; i++ )
					cout<<p[i]<<"\n";
				cout<<"\n\n Enter an item to be searched: ";
				cin>>fele;				
				b.Bsearch(p,fele,N);
				break;
			}
		case 2:
			{
				string *q=new string[N];
				string sele;
				cout<<"\nEnter "<<N<<" strings..\n";
				for(i=0; i<N; i++ )
					cin>>q[i];
				cout<<"\nArray before sorting is..\n";
				for(i=0; i<N; i++ )
					cout<<q[i]<<"\n";
				b.Quick( q,0,N-1 );
				cout<<"\nArray after sorting is..\n";
				for(i=0; i<N; i++ )
					cout<<q[i]<<"\n";
				cout<<"\n\n Enter an item to be searched: ";
				cin>>sele;				
				b.Bsearch(q,sele,N);
				break;
			}
	}
	return 0;
}
