class pe10
{
	static boolean prime(long n)
	{
		for(long i=2;i<n;i++)
			if(n%i==0)
				return false;
		return true;
	}

	public static void main(String args[])
	{
		long i,s=2;
		for(i=3;i<2000000;i+=2)
			if(prime(i)==true)
				s+=i;
		System.out.print(s);
	}
}