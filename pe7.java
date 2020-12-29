class pe7
{
	static boolean prime(int n)
	{
		for(int i=2;i<n;i++)
			if(n%i==0)
				return false;
		return true;
	}
	public static void main(String args[])
	{
		int i=1,n=1;
		while(n!=10001)
		{
			i+=2;
			if(prime(i)==true)
				n+=1;
		}
		System.out.print(i);
	}
}