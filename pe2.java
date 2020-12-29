class pe2
{
	public static void main(String args[])
	{
		int s=0,a=0,b=1,c=1;
		while(c<=4000000)
		{
			if(c%2==0)
				s+=c;
			a=b;
			b=c;
			c=a+b;
		}
		System.out.print(s);
	}
}