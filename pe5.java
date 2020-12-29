class pe5
{
	public static void main(String args[])
	{
		int i,n=2520,flag=0;
		while(flag==0)
		{
			n+=20;
			flag=1;
			for(i=2;i<=20;i++)
				if(n%i!=0)
				{
					flag=0;
					break;
				}
		}
		System.out.print(n);
	}
}