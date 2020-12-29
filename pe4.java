class pe
{
	static boolean palindrome(int n)
	{
		int newn=0,dup=n;
		while(n>0)
		{
			newn=(newn*10)+(n%10);
			n/=10;
		}
	if(newn==dup)
		return true;
	return false;
	}

	public static void main(String args[])
	{
		int maxp=0,p,i,j;
		for(i=100;i<1000;i++)
			for(j=100;j<1000;j++)
			{
				p=i*j;
				if(p>maxp && palindrome(p)==true)
					maxp=p;
			}
		System.out.print(maxp);
	}
}